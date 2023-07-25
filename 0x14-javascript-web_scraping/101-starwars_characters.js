#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

function getMovieCharacters(movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;
      const characterNames = [];

      let count = 0;

      function fetchCharacter(characterUrl) {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
          } else {
            const characterData = JSON.parse(body);
            characterNames.push(characterData.name);

            count++;

            if (count === characters.length) {
              characterNames.forEach((name) => {
                console.log(name);
              });
            }
          }
        });
      }

      characters.forEach((characterUrl) => {
        fetchCharacter(characterUrl);
      });
    }
  });
}

getMovieCharacters(movieId);
