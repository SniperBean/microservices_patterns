import { getPubSub } from '../kafka-driver.mjs';
import { host, port } from './config.mjs';

export const testSub = getPubSub(
    'test-topic',
    host,
    port,
    {}
)

export const userSub = getPubSub(
    'user-reply',
    host,
    port,
    {}
)

export const itemSub = getPubSub(
    'item-reply',
    host,
    port,
    {}
)

export const orderSub = getPubSub(
    'order-reply',
    host,
    port,
    {}
)