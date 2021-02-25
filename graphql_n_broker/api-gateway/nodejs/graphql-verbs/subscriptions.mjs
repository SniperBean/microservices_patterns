import { getPubSub } from '../kafka-pubsub-engine/kafka-driver.mjs';
import filter from 'apollo-server'
const { withFilter } = filter;

export function getTestSub (_, args, context) {
    const pubsub = getPubSub(
        'test-topic',
        'kafka',
        '9092',
        {}
    )

    return withFilter(
        (_, args, context) => pubsub.asyncIterator(['GET_USER']),
        (payload, context) => {
            return payload.getTest.msgID === context.msgID;
        });

}