import { hello } from '../graphql-verbs/queries.mjs';
import { getTestMut } from '../graphql-verbs/mutations.mjs';
import { getTestSub } from '../graphql-verbs/subscriptions.mjs';

export const resolvers = {
    Query: {
        hello: () => hello()
    },
    Mutation: {
        getTest: (_, args, context) => getTestMut(_, args, context)
    },
    Subscription: {
        getTest: {
            subscribe: getTestSub()
        }
    }
};