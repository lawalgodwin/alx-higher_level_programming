#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    let breadth = '';

    let printChar = c || undefined;
    if (!printChar) printChar = 'X';

    for (let i = 0; i < this.width; i++) breadth += printChar;

    for (let j = 0; j < this.width; j++) console.log(breadth);
  }
}

module.exports = Square;
