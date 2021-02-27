import { testSub, userSub, itemSub, orderSub } from '../kafka-pubsub-engine/pubsub/subscription.mjs';
import filter from 'apollo-server'
const { withFilter } = filter;


export function getTestSub (_, args, context) {
    return withFilter(
        (_, args, context) => testSub.asyncIterator(['GET_TEST']),
        (payload, context) => {
            return payload.getTest.msg_id === context.msg_id;
        });

}

export function getUserSub (_, args, context) {
    return withFilter(
        (_, args, context) => userSub.asyncIterator(['GET_USER']),
        (payload, context) => {
            return payload.user.msg_id === context.msg_id;
        });
}

export function getUsersSub (_, args, context) {
    return withFilter(
        (_, args, context) => userSub.asyncIterator(['GET_USERS']),
        (payload, context) => {
            return payload.users.msg_id === context.msg_id;
        });
}

export function getItemSub (_, args, context) {
    return withFilter(
        (_, args, context) => itemSub.asyncIterator(['GET_ITEM']),
        (payload, context) => {
            return payload.item.msg_id === context.msg_id;
        });
}

export function getItemsSub (_, args, context) {
    return withFilter(
        (_, args, context) => itemSub.asyncIterator(['GET_ITEMS']),
        (payload, context) => {
            return payload.items.msg_id === context.msg_id;
        });
}

export function getOrdersSub (_, args, context) {
    return withFilter(
        (_, args, context) => orderSub.asyncIterator(['GET_ORDERS']),
        (payload, context) => {
            return payload.orders.msg_id === context.msg_id;
        });
}