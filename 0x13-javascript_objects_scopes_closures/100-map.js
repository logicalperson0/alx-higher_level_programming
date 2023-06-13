#!/usr/bin/node
const list = require('./100-data').list;
const mapping = list.map((currEle, index) => {
  return (currEle = currEle * index);
});
console.log(list);
console.log(mapping);
