#!/usr/bin/node

const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '555-555-5555',
    message: 'Hello'
}

const myJob = queue.create("push_notification_code", jobData);

myJob
  .on("enqueue", () => {
    console.log(`Notification job created: ${myJob.id}`);
  })
  .on("failed", (job, err) => {
    console.log("Notification job failed");
  })
  .on("complete", (job, result) => {
    console.log("Notification job completed");
  });

myJob.save();