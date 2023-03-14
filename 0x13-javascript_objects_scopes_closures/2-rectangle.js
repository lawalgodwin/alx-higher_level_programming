#!/usr/bin/node
/*  Create an empty object if h or w is -ve or 0  */
class Rectangle {
  constructor (w, h) {
    if (!isNaN(w) && (w > 0) && !isNaN(h) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
