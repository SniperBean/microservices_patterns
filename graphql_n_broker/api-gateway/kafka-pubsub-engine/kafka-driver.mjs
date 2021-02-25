import kafka_pub_sub from 'graphql-kafka-subscriptions'
const {KafkaPubSub} = kafka_pub_sub;

export function getPubSub (topic, host, port, globalConfig = {}) {
    return new KafkaPubSub({
        topic: topic,
        host: host,
        port: port,
        globalConfig: globalConfig // options passed directly to the consumer and producer
    });
}

const onMessage = (payload) => {
    // console.log(payload);
}