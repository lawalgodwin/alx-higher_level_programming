#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode
// number matches a given integer

const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, res, body) => {
  if (err) return console.error(err);
  console.log(JSON.parse(body).title);
});
