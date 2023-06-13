#!/usr/bin/node
let j = -1;
exports.logMe = function (item) {
  for (let i = 0; i < arguments.length; i++) {
    j += 1;
    console.log(j + ': ' + item);
  }
};
