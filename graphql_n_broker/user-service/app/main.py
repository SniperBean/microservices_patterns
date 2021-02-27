from kafka import (
    KafkaAdminClient,
    KafkaConsumer,
    KafkaProducer
)

from kafka.admin import NewTopic

dummy_list = [
        {
            "id": "1",
            "name": "Jose Miguel"
        },
        {
            "id": "2",
            "name": "Souch Hsu"
        },
        {
            "id": "3",
            "name": "John Cena"
        },
        {
            "id": "4",
            "name": "Takahashi Hitoshi"
        },
        {
            "id": "5",
            "name": "Elon Musk"
        }
    ]


ORDER_REQUEST_TOPIC = 'order-request'
USER_REQUEST_TOPIC = 'user-request'
USER_REPLY_TOPIC = 'user-reply'


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
    msg = {
        "users": {
            "msg_id": payload['msg_id'],
            "msg": dummy_list
        }
    }
    produce_event(ORDER_REQUEST_TOPIC, event['channel'], msg, aggregation_id=event['aggregation_id'])


def get_users(event):
    channel = event['channel']
    payload = event['payload']
    msg = {
        'users': {
            "msg_id": payload['msg_id'],
            "msg": dummy_list
        }
    }
    produce_event(USER_REPLY_TOPIC, channel, msg)


def get_user(event):
    channel = event['channel']
    payload = event['payload']
    user = {}
    for item in dummy_list:
        if item['id'] == str(payload['id']):
            user = item
    msg = {
        "user": {
            "msg_id": payload['msg_id'],
            "msg": user
        }
    }
    produce_event(USER_REPLY_TOPIC, channel, msg)


def event_etl(consumer):
    for msg in consumer:
        try:
            event = eval(str(msg.value, 'utf-8'))
            channel = event['channel']
            payload = event['payload']
            if channel == 'GET_ORDERS':
                set_orders(event)
            elif 'id' in payload:
                get_user(event)
            else:
                get_users(event)

        except Exception as e:
            print(e)


def main():
    try:
        admin = KafkaAdminClient(bootstrap_servers='kafka:9092')

        topics = [
            NewTopic(
                name=USER_REQUEST_TOPIC,
                num_partitions=1,
                replication_factor=1
            ),
            NewTopic(
                name=USER_REPLY_TOPIC,
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
    consumer.subscribe(USER_REQUEST_TOPIC)

    while True:
        event_etl(consumer)


if __name__ == "__main__":
    main()

