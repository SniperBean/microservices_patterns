from kafka import (
    KafkaAdminClient,
    KafkaConsumer,
    KafkaProducer
)

from kafka.admin import NewTopic

dummy_dict = {
    "item-1": {"name": "Microservice patterns", "detail": "Introduce modern architecture pattern."},
    "item-2": {"name": "Release it! 2nd edition", "detail": "Case study and consulting skills share."},
    "item-3": {"name": "Designing Event-Driven Systems", "detail": "Design event-driven architecture in action."}
}

ORDER_REQUEST_TOPIC = 'order-request'
ITEM_REQUEST_TOPIC = 'item-request'
ITEM_REPLY_TOPIC = 'item-reply'


def produce_event(topic, channel, msg, aggregation_id=None):
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    msg = {
        "channel": channel,
        "payload": msg
    }

    if aggregation_id:
        msg.update({"aggregation_id": aggregation_id})

    producer.send(
        topic,
        str.encode(str(msg).replace("'", '"'))
    )


def set_orders(event):
    payload = event['payload']
    dummy_list = []
    for item_id, data in dummy_dict.items():
        dummy_list.append({"item_id": item_id, "data": data})
    msg = {
        "items": {
            "msg_id": payload['msg_id'],
            "msg": dummy_list
        }
    }
    produce_event(ORDER_REQUEST_TOPIC, event['channel'], msg, aggregation_id=event['aggregation_id'])


def get_items(event):
    channel = event['channel']
    payload = event['payload']
    dummy_list = []
    for item_id, data in dummy_dict.items():
        dummy_list.append({"item_id": item_id, "data": data})
    msg = {
        "items": {
            "msg_id": payload['msg_id'],
            "msg": dummy_list
        }
    }
    produce_event(ITEM_REPLY_TOPIC, channel, msg)


def get_item(event):
    channel = event['channel']
    payload = event['payload']
    msg = {
        "item": {
            "msg_id": payload['msg_id'],
            "msg": {"item_id": payload['item_id'], "data": dummy_dict[payload['item_id']]}
        }
    }
    produce_event(ITEM_REPLY_TOPIC, channel, msg)


def event_etl(consumer):
    for msg in consumer:
        try:
            event = eval(str(msg.value, 'utf-8'))
            channel = event['channel']
            payload = event['payload']
            if channel == 'GET_ORDERS':
                set_orders(event)
            elif 'item_id' in payload:
                get_item(event)
            else:
                get_items(event)

        except Exception as e:
            print(str(e))


def main():
    try:
        admin = KafkaAdminClient(bootstrap_servers='kafka:9092')

        topics = [
            NewTopic(
                name=ITEM_REQUEST_TOPIC,
                num_partitions=1,
                replication_factor=1
            ),
            NewTopic(
                name=ITEM_REPLY_TOPIC,
                num_partitions=1,
                replication_factor=1
            )
        ]
        admin.create_topics(topics)
    except Exception:
        pass

    consumer = KafkaConsumer(
        auto_offset_reset='earliest',
        consumer_timeout_ms=1000,
        group_id='item-service',
        bootstrap_servers=['kafka:9092']
    )
    consumer.subscribe(ITEM_REQUEST_TOPIC)

    while True:
        event_etl(consumer)


if __name__ == "__main__":
    main()

