#!/usr/bin/node
/* script that prints the title of a Star Wars movie where the episode number
  matches a given integer. */

  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

  const request = require('request');
  request(url, function (error) {
    if (error) {
      console.log(error);
    }
    console.log(JSON.parse(response.body).title);
  });
  