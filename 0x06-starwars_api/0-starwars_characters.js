#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + movieId,
  method: 'GET'
};

request(options, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const chars = JSON.parse(body).characters;
    if (chars && chars.length > 0) {
      printChars(chars, 0);
    } else {
      console.error('No characters found for the given movie.');
    }
  } else {
    console.error('Error:', error || `Status code: ${response.statusCode}`);
  }
});

function printChars(chars, idx) {
  request(chars[idx], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < chars.length) {
        printChars(chars, idx + 1);
      }
    } else {
      console.error(
        'Error fetching character:', error ||
        `Status code: ${response.statusCode}`);
    }
  });
}
