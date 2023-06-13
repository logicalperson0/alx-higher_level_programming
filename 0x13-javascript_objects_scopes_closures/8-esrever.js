#!/usr/bin/node
exports.esrever = function (list) {
  const x = [];
  let y = -1;
  for (let i = 0; i < list.length; i++) {
    y += 1;
  }
  for (let j = 0; j < list.length; j++, y--) {
    x[j] = list[y];
  }
  return (x);
};
