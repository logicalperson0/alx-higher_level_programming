#!/usr/bin/node
const val = parseInt(process.argv[2]);
if (isNaN(Number(val))) {
  console.log('Not a number');
} else {
  console.log(val);
}
