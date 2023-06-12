#!/usr/bin/node
let arr = '';
const val = parseInt(process.argv[2]);
if (isNaN(Number(val))) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= val; i++) {
    for (let j = 1; j <= val; j++) {
      arr += 'X';
    }
    console.log(arr);
    arr = '';
  }
}
