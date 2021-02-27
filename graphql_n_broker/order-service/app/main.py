import hashlib
import copy
from kafka import (
    KafkaAdminClient,
    KafkaConsumer,
    KafkaProducer
)
from uuid import uuid4
from kafka.admin import NewTopic

dummy_list = [
        {
            'order_id': 1,
            'user': '1',
            'item': 'item-1',
            'quantity': 1
        },
        {
            'order_id': 2,
            'user': '1',
            'item': 'item-2',
            'quantity': 1
        },
        {
            'order_id': 3,
            'user': '1',
            'item': 'item-3',
            'quantity': 1
        },
        {
            'order_id': 4,
            'user': '2',
            'item': 'item-1',
            'quantity': 3
        },
        {
            'order_id': 5,
            'user': '3',
            'item': 'item-2',
            'quantity': 1
        },
        {
            'order_id': 6,
            'user': '3',
            'item': 'item-3',
            'quantity': 1
        },
        {
            'order_id': 7,
            'user': '4',
            'item': 'item-3',
            'quantity': 1
        },
        {
            'order_id': 8,
            'user': '5',
            'item': 'item-2',
            'quantity': 1
        }
    ]

ORDER_REQUEST_TOPIC = 'order-request'
USER_REQUEST_TOPIC = 'user-request'
ITEM_REQUEST_TOPIC = 'item-request'
ORDER_REPLY_TOPIC = 'order-reply'

event_heap = {}


def produce_event(topic, channel, msg, aggregation_id=None):
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'])
    msg = {
        'channel': channel,
        'payload': msg
    }

    if aggregation_id:
        msg.update({'aggregation_id': aggregation_id})

    producer.send(
        topic,
        str.encode(str(msg).replace("'", '"'))
    )


def get_users(event, aggregation_id):
    msg = event['payload']
    produce_event(USER_REQUEST_TOPIC, event['channel'], msg, aggregation_id)


def get_items(event, aggregation_id):
    msg = event['payload']
    produce_event(ITEM_REQUEST_TOPIC, event['channel'], msg, aggregation_id)


def get_orders(event):
    if event['aggregation_id'] in event_heap:
        mapping_list = copy.deepcopy(dummy_list)
        users, items, msg_id = shuffle_heap(event_heap[event['aggregation_id']], event['payload'])
        for order in mapping_list:
            order['user'] = next(user for user in users if user['id'] == str(order['user']))
            order['item'] = next(item for item in items if item['item_id'] == str(order['item']))
        msg = {
            'orders': {
                'msg_id': msg_id,
                'msg': mapping_list
            }
        }
        produce_event(ORDER_REPLY_TOPIC, event['channel'], msg)
    else:
        event_heap.update({event['aggregation_id']: event['payload']})


def shuffle_heap(obj1, obj2):
    users = obj1 if 'users' in obj1 else obj2
    items = obj2 if 'users' in obj1 else obj1
    msg_id = users['users']['msg_id'] if users['users']['msg_id'] == items['items']['msg_id'] else None
    users = users['users']['msg']
    items = items['items']['msg']
    print(users)
    print(items)
    return users, items, msg_id


def event_etl(consumer):
    for msg in consumer:
        try:
            event = eval(str(msg.value, 'utf-8'))
            payload = event['payload']
            if 'aggregation_id' in event:
                get_orders(event)
            else:
                sha = hashlib.sha1()
                data = str.encode(str(uuid4()))
                sha.update(data)
                aggregation_id = sha.hexdigest()
                get_users(event, aggregation_id)
                get_items(event, aggregation_id)

        except KeyError as e:
            print(e)


def main():
    try:
        admin = KafkaAdminClient(bootstrap_servers='kafka:9092')

        topics = [
            NewTopic(
                name=ORDER_REQUEST_TOPIC,
                num_partitions=1,
                replication_factor=1
            ),
            NewTopic(
                name=ORDER_REPLY_TOPIC,
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
        group_id='order-service',
        bootstrap_servers=['kafka:9092']
    )
    consumer.subscribe(ORDER_REQUEST_TOPIC)

    while True:
        event_etl(consumer)


if __name__ == '__main__':
    main()

