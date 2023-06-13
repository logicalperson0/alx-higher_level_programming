#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || h === undefined || w === undefined) {
      w = {};
      h = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        x += 'X';
      }
      console.log(x);
      x = '';
    }
  }

  rotate () {
    let d = 0;
    d = this.height;
    this.height = this.width;
    this.width = d;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
