#!/usr/bin/node
exports.converter = function (base) {
  return function converter (num) {
    /* return parseInt(num + '', base); */
    return num.toString(base);
  };
};
