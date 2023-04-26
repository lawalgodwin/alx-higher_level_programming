#!/usr/bin/node
// A script that computes the number of tasks completed by user id

const request = require('request');

request(`${process.argv[2]}`, { json: true }, (err, res, body) => {
  if (err) return console.error(err);
  const completed = body.filter((task) => task.completed === true);
  const completedTask = {};
  completed.forEach(task => {
    if (!completedTask[task.userId]) { completedTask[task.userId] = 1; } else { completedTask[task.userId] += 1; }
  });
  console.log(completedTask);
});
