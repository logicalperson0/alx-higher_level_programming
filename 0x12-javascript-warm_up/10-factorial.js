#!/usr/bin/node
const val = parseInt(process.argv[2]);
const val1 = factorial(val);
console.log(val1);
function factorial (a) {
  if (isNaN(Number(a))) {
    return 1;
  } else if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
