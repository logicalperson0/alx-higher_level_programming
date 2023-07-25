#!/usr/bin/node
const requesting = require('request');
const urls = process.argv[2];
const dict = {};

requesting(urls, (error, response, body) => {
  if (error) console.log(error);

  const parsing = JSON.parse(body);

  for (let x = 0; x < parsing.length; x++) {
    if (parsing[x].completed === true) {
      if (dict[parsing[x].userId] === undefined) {
        dict[parsing[x].userId] = 0;
      } else {
        dict[parsing[x].userId]++;
      }
    }
  }
  console.log(dict);
});
