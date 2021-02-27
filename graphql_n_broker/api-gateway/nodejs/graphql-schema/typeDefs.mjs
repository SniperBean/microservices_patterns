import apollo from 'apollo-server';
const { gql } = apollo;

export const typeDefs = gql`
  type Query {
    hello: String
  }
  
  type Mutation {
    getTest (msg: String, msg_id: String): String
    getUser (id: ID, msg_id: String): String
    getUsers (msg_id: String): String
    getItem (item_id: ID, msg_id: String): String
    getItems (msg_id: String): String
    getOrders (msg_id: String): String
  }
  
  type Subscription {
    getTest (msg_id: String): Message
    user (msg_id: String): UserEvent
    users (msg_id: String): UsersEvent
    item (msg_id: String): ItemEvent
    items (msg_id: String): ItemsEvent
    orders (msg_id: String): OrdersEvent
  }
  
  type Message {
    msg_id: String
    msg: String
  }
  
  type UserEvent{
    msg_id: String
    msg: User
  }
  
  type UsersEvent{
    msg_id: String
    msg: [User]
  }
  
  type ItemEvent{
    msg_id: String
    msg: Item
  }
  
  type ItemsEvent{
    msg_id: String
    msg: [Item]
  }
  
  type OrdersEvent{
    msg_id: String
    msg: [Order]
  }
  
  type User {
      id: ID!
      name: String!
  }
  
  type Item {
    item_id: ID
    data: item_data
  }

  type item_data {
    name: String!
    detail: String!
  }
  
  type Order {
    order_id: ID
    user: User
    item: Item
    quantity: Int
  }
`;