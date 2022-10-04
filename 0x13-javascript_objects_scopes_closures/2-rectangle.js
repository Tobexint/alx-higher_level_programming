#!/usr/bin/node
// The constructor must take 2 arguments w and h
// Initialize the instance attribute width with the value of w
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
