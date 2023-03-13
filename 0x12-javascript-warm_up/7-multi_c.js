#!/usr/bin/node

let i = 0;

const firstArg = process.argv[2];

if (process.argv.length < 3) console.log('Missing number of occurrences');

if (isNaN(firstArg)) process.exit();

else {
  while (true) {
    if (i >= parseInt(firstArg)) process.exit();
    console.log('C is fun');
    i += 1;
  }
}
