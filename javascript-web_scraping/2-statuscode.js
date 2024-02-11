#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the URL to request from the first argument
const url = process.argv[2];

// Make a GET request to the URL
request.get(url, (err, response) => {
  // If an error occurred, print the error object
  if (err) {
    console.error(err);
  } else {
    // Otherwise, print the status code like this: code: <status code>
    console.log(`code: ${response.statusCode}`);
  }
});
