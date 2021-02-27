import { hello } from '../graphql-verbs/queries.mjs';
import { getTestMut, getItemMut, getItemsMut, getUserMut, getUsersMut, getOrdersMut } from '../graphql-verbs/mutations.mjs';
import { getTestSub, getItemSub, getItemsSub, getUserSub, getUsersSub, getOrdersSub } from '../graphql-verbs/subscriptions.mjs';

export const resolvers = {
    Query: {
        hello: () => hello()
    },
    Mutation: {
        getTest: (_, args, context) => getTestMut(_, args, context),
        getItem: (_, args, context) => getItemMut(_, args, context),
        getItems: (_, args, context) => getItemsMut(_, args, context),
        getUser: (_, args, context) => getUserMut(_, args, context),
        getUsers: (_, args, context) => getUsersMut(_, args, context),
        getOrders: (_, args, context) => getOrdersMut(_, args, context)
    },
    Subscription: {
        getTest: {
            subscribe: getTestSub()
        },
        user: {
            subscribe: getUserSub()
        },
        users: {
            subscribe: getUsersSub()
        },
        item: {
            subscribe: getItemSub()
        },
        items: {
            subscribe: getItemsSub()
        },
        orders: {
            subscribe: getOrdersSub()
        }
    }
};