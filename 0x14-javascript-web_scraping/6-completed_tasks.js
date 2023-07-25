#!/usr/bin/node
const requesting = require('request');
const urls = process.argv[2];
const dict = {};

requesting(urls, (error, response, body) => {
  if (error) console.log(error);

  const parsing = JSON.parse(body);

  for (const x of parsing) {
    if (x.completed === true) {
      if (dict[x.userId] === undefined) {
        dict[x.userId] = 1;
      } else {
        dict[x.userId]++;
      }
    }
  }
  console.log(dict);
});
