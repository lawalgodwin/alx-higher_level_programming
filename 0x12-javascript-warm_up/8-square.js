#!/usr/bin/node

const firstArg = process.argv[2];
let row = '';
const printChar = 'X';

if (!firstArg || isNaN(firstArg)) console.log('Missing size');

else {
  for (let i = 0; i < firstArg; i++) {
    row += printChar;
  }
  for (let j = 0; j < firstArg; j++) console.log(row);
}
