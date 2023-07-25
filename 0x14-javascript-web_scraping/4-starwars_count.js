#!/usr/bin/node
const requesting = require('request');
const UrlStarwars = process.argv[2];
let IDLength = 0;

requesting(UrlStarwars, (error, response, body) => {
  if (error) console.log(error);

  const parsing = JSON.parse(body);

  const actor = parsing.results;

  for (let x = 0; x < actor.length; x++) {
    for (let y = 0; y < actor[x].characters.length; y++) {
      if (actor[x].characters[y].includes('18', 0) === true) {
        IDLength++;
      }
    }
  }
  console.log(IDLength);
});
