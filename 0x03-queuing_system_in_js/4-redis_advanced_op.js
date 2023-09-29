#!/usr/bin/node
// Storing hash values in redis
import { createClient } from 'redis';
const redis = require('redis');

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const hashObject = {
        'Portland': 50,
        'Seattle': 80,
        'New York': 20,
        'Bogota': 20,
        'Cali': 40,
        'Paris': 2
}

for (const key in hashObject) {
  client.hset('HolbertonSchools', key, hashObject[key], redis.print);
};

client.hgetall('HolbertonSchools', (err, obj) => {
  console.log(obj);
});