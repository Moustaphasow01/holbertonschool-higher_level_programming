#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles”
  is present. */

  const url = process.argv[2];
  let contador = 0;
  
  const request = require('request');
  request(url, function (error, response) {
    if (error) {
      console.log(error);
    }
    const results = (JSON.parse(response.body).results);
    results.forEach(element => {
      element.characters.forEach(people => {
        if (people.search('18') !== -1) {
          contador += 1;
        }
      });
    });
    console.log(contador);
  });
  