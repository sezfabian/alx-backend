#!/usr/bin/node
// Storing hash values in redis
import { createClient } from 'redis';
const redis = require('redis');

const subscriber = createClient();

subscriber.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
        console.log(message);
        if (message === "KILL_SERVER") {
            subscriber.unsubscribe();
            subscriber.quit();
        }
    });