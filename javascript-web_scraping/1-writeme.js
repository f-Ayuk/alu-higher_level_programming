#!/usr/bin

// Import the file system module
const fs = require('fs');

// Get the file path from the first argument
const filePath = process.argv[2];

// Get the string to write from the second argument
const string = process.argv[3];

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, string, 'utf8', (err) => {
  // If an error occurred, print the error object
  if (err) {
    console.error(err);
  }
});
