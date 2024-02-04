#!/usr/bin/node
// Define the class Rectangle
class Rectangle {
  // Define the constructore with two parameters w and h
  constructor(w, h) {
    // check if w and h are positive integers
    if (w > 0 && h > 0) {
      // initialise the instance
      this.width = w;
      this.height = h;
        } else {
            return {};
        }
    }
}

module.exports = Rectangle;
