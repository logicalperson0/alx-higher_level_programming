#!/usr/bin/node
const requesting = require('request');
const urls = 'https://swapi-api.alx-tools.com/api/films/';
let characters = [];
let id = parseInt(process.argv[2], 10);

requesting(urls, function (error, response, body) {
  if (error == null) {
    const resp = JSON.parse(body);
    const results = resp.results;
    if (id < 4) {
      id += 3;
    } else {
      id -= 3;
    }
    for (const i of results) {
      if (i.episode_id === id) {
        characters = i.characters;
        break;
      }
    }
    for (const j of characters) {
      requesting(j, function (error, response, body) {
        if (error == null) {
          const people = JSON.parse(body).name;

          console.log(people);
        }
      });
    }
  }
});
