#!/usr/bin/node
/*  Create an empty object if h or w is -ve or 0  */
class Rectangle {
  constructor (w, h) {
    if ((typeof w === 'number') && (w > 0) && (typeof h === 'number') && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let breadth = '';

    for (let i = 0; i < this.width; i++) breadth += 'X';

    for (let j = 0; j < this.height; j++) console.log(breadth);
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}

module.exports = Rectangle;
