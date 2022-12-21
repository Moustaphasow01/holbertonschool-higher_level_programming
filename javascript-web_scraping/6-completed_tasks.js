#!/usr/bin/node
/* script that computes the number of tasks completed by user id. */

const request = require('request');
const url = process.argv[2];
const list = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(response.body);
  data.forEach(element => {
    if (element.completed === true) {
      list[element.userId] += 1;
    }
  });
  console.log(list);
});
