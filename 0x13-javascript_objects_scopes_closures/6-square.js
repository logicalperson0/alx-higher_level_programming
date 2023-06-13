#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let x = '';
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        x += c;
      }
      console.log(x);
      x = '';
    }
  }
}

module.exports = Square;
