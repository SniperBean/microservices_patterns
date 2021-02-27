import { testPub, userPub, itemPub, orderPub } from '../kafka-pubsub-engine/pubsub/publish.mjs';

export async function getTestMut (_, args, context) {
    await testPub.publish(
        'GET_TEST',
        {
            getTest: {
                msg: args['msg'],
                msg_id: args['msg_id']
            }
        });
    return "OK";
}

export async function getUserMut (_, args, context) {
    await userPub.publish(
        'GET_USER',
        {
            id: args['id'],
            msg_id: args['msg_id']
        });
    return "OK";
}

export async function getUsersMut (_, args, context) {
    await userPub.publish(
        'GET_USERS',
        {
            msg_id: args['msg_id']
        });
    return "OK";
}

export async function getItemMut (_, args, context) {
    await itemPub.publish(
        'GET_ITEM',
        {
            item_id: args['item_id'],
            msg_id: args['msg_id']
        });
    return "OK";
}

export async function getItemsMut (_, args, context) {
    await itemPub.publish(
        'GET_ITEMS',
        {
            msg_id: args['msg_id']
        });
    return "OK";
}

export async function getOrdersMut (_, args, context) {
    await orderPub.publish(
        'GET_ORDERS',
        {
            msg_id: args['msg_id']
        });
    return "OK";
}