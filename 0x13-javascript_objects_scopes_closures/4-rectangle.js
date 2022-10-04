#!/usr/bin/node
class Rectangle {
/* The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h */
  // If w or h is equal to 0 or not a positive integer, create an empty object
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  /* Create an instance method called print() that prints the rectangle using the character X */
  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  /* Create an instance method called rotate() that exchanges the width and the height of the rectangle */
  rotate () {
    const h = this.height;
    const w = this.width;
    this.width = h;
    this.height = w;
  }

  /* Create an instance method called double() that multiples the width and the height of the rectangle by 2 */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
