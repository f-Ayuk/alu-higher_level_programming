#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

// Define the character ID of Wedge Antilles
const wedgeId = 18;

// Make a GET request to the API
request(apiUrl, function (error, response, body) {
  if (!error) {
    // If the request was successful, count the movies
    // Parse the JSON data from the body
    const data = JSON.parse(body);

    // Get the array of movies from the data
    const movies = data.results;

    // Initialize a counter for the movies with Wedge Antilles
    let count = 0;

    // Loop through the movies
    for (const movie of movies) {
      // Get the array of characters from the movie
      const characters = movie.characters;

      // Check if Wedge Antilles is in the characters array
      if (characters.includes(`https://swapi-api.alx-tools.com/api/films/${wedgeId}/`)) {
        // Increment the counter
        count++;
      }
    }

    // Print the number of movies with Wedge Antilles
    console.log(count);
  } else {
    // Otherwise, print an error message
    console.error(`Error: ${response.statusCode}`);
  }
});
