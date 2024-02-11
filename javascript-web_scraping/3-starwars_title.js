#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the movie ID from the first argument
const movieId = process.argv[2];

// Construct the API URL with the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API
request(apiUrl, ;(error, response, body) => {
  // If the request was successful, print the movie title
  if (response.statusCode === 200) {
    // Parse the JSON data from the body
    const data = JSON.parse(body);

    // Get the movie title from the data
    const movieTitle = data.title;

    // Print the movie title
    console.log(movieTitle);
  } else {
    // Otherwise, print an error message
    console.error(`Error: ${response.statusCode}`);
  }
});
