#!/usr/bin/node
const val1 = process.argv[2];
const val2 = process.argv[3];
add(val1, val2);
function add (a, b) {
  const val1 = parseInt(a);
  const val2 = parseInt(b);
  console.log(val1 + val2);
}
