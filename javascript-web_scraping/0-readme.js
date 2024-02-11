#!/usr/bin/node

// Import the file system module
const fs = require('fs');

// Get the file path from the first argument
const filePath = process.argv[2];

// Read the file in utf-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  // If an error occurred, print the error object
  if (err) {
    console.error(err);
  } else {
    // Otherwise, print the file content
    console.log(data);
  }
});
