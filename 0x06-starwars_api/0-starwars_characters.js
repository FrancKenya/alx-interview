#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).chars;
    printChars(chars, 0);
  }
});

function printChars (chars, idx) {
  request(chars[idx], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < chars.length) {
        printChars(chars, idx + 1);
      }
    }
  });
}
