#!/usr/bin/node
const a = process.argv;
let max = 0;
let sec = 0;
if (a.length <= 2) {
  console.log('0');
} else {
  for (let i = 2; i < a.length; i++) {
    if (a[i] > max) {
      sec = max;
      max = a[i];
    } else if (a[i] > sec && a[i] !== max) {
      sec = a[i];
    }
  }
  console.log(sec);
}
