import apollo from 'apollo-server';
const { gql } = apollo;

export const typeDefs = gql`
  type Query {
    hello: String
  }
  
  type Mutation {
    getTest (msg: String, msgID: String): String
  }
  
  type Subscription {
    getTest (msgID: String): MESSAGE
  }
  
  type MESSAGE {
    msgID: String
    msg: String
  }
`;