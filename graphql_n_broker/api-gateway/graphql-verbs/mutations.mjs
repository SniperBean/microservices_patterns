import { getPubSub } from '../kafka-pubsub-engine/kafka-driver.mjs';

export async function getTestMut (_, args, context) {
    const pubsub = getPubSub(
        'my-first-application',
        '127.0.0.1',
        '9092',
        {}
    )

    await pubsub.publish(
        'GET_USER',
        {
            getTest: {
                msg: args['msg'],
                msgID: args['msgID']
            }
        });
    return "OK";
}
