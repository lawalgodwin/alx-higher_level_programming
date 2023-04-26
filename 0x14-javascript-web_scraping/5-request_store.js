#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');

request(`${process.argv[2]}`, (err, res, body) => {
  if (err) return console.error(err);
  fs.writeFile(`${process.argv[3]}`, body, 'utf-8', (err) => console.error(err))
})
