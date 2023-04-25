#!/usr/bin/node
// A script that prints the number of movies where the
// character “Wedge Antilles” is present.
// Wedge Antilles is character ID 18
//  Star wars API: https://swapi-api.alx-tools.com/api/films/

const request = require('request');

request(`${process.argv[2]}`, (err, res, body) => {
  if (err) return console.error(err);
  const films = JSON.parse(body).results;
  let count = 0;
  const characterId = 18;
  films.forEach((film) => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) { count += 1; }
  });
  console.log(count);
});
