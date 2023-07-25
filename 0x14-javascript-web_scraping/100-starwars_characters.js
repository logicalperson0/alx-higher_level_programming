#!/usr/bin/node
const requesting = require('request');
const UrlStarwars = 'https://swapi-api.alx-tools.com/api/films/';
const ID = process.argv[2];

requesting(UrlStarwars + ID, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const actors = JSON.parse(body).characters;

    for (let x = 0; x < actors.length; x++) {
      requesting(actors[x], (error, response, body) => {
        if (error) console.log(error);

        const people = JSON.parse(body).name;

        console.log(people);
      });
    }
  }
});
