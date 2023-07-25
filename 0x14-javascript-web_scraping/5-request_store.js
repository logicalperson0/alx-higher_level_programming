#!/usr/bin/node
const requesting = require('request');
const Urls = process.argv[2];
const FilePath = process.argv[3];
const file = require('fs');

requesting(Urls, (error, response, body) => {
  if (error) console.log(error);

  file.writeFile(FilePath, body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
