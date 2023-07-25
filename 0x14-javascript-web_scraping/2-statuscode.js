#!/usr/bin/node
const requesting = require('request');
const urls = process.argv[2];

requesting(urls, (error, response) => {
  if (error) console.log(error);

  console.log('code' + ': ' + response.statusCode);
});
