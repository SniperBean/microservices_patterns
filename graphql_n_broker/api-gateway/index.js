import apollo from 'apollo-server';
import { resolvers } from "./graphql-schema/resolvers.mjs";
import { typeDefs } from "./graphql-schema/typeDefs.mjs";
const {ApolloServer} = apollo;

const server = new ApolloServer({
  typeDefs,
  resolvers,
});

server.listen().then(({ url }) => {
  console.log(`Server ready at ${url}`);
});
