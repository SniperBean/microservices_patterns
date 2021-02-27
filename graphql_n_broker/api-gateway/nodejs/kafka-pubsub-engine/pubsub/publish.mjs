import { getPubSub } from '../kafka-driver.mjs';
import { host, port } from './config.mjs';

export const testPub = getPubSub(
    'test-topic',
    host,
    port,
    {}
)

export const userPub = getPubSub(
    'user-request',
    host,
    port,
    {}
)

export const itemPub = getPubSub(
    'item-request',
    host,
    port,
    {}
)

export const orderPub = getPubSub(
    'order-request',
    host,
    port,
    {}
)