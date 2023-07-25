#!/usr/bin/node
const requesting = require('request');
const UrlStarwars = 'https://swapi-api.alx-tools.com/api/films/';
const ID = process.argv[2];

requesting(UrlStarwars + ID, (error, response, body) => {
  if (error) console.log(error);

  const TitleStar = JSON.parse(body);

  console.log(TitleStar.title);
});
