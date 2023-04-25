#!/usr/bin/node
// A script that reads the content of a file and output it to stdout

const fs = require('fs');

fs.open(`${process.argv[2]}`, 'r', (err, fd) => {
  if (err) return console.error(err);
  fs.readFile(fd, 'utf-8', (err, data) => {
    if (err) return console.error(err);
    console.log(data);
  });
});
