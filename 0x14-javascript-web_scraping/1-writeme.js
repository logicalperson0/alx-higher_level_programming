#!/usr/bin/node
const file = require('fs');
const InputFile = process.argv[2];
const InputData = process.argv[3];
file.writeFile(InputFile, InputData, 'utf-8', (err) => {
  if (err) throw err;
});
