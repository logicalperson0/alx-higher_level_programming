#!/usr/bin/node
const requesting = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const ID = process.argv[2];

requesting(url + ID, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    characters.forEach((character) => {
      requesting(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const characterName = JSON.parse(body);
          console.log(characterName.name);
        }
      });
    });
  }
});
