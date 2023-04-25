#!/usr/bin/node
// A script that writes a string to a file

const fs = require('fs');

fs.open(`${process.argv[2]}`, 'w', (err, fd) => {
  if (err) { return console.error(err); }
  fs.writeFile(fd, `${process.argv[3]}`, 'utf-8', (err) => {
    if (err) { console.error(err); }
  });
});
