#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

// Define the character ID of Wedge Antilles
const wedgeId = 18;

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  // If the request was successful, count the movies
  if (response.statusCode === 200) {
    // Parse the JSON data from the body
    const data = JSON.parse(body);

    // Get the array of movies from the data
    const movies = data.results;

    // Initialize a counter for the movies with Wedge Antilles
    let count = 0;

    // Loop through the movies
    for (const movie of movies = movies) {
      // Get the array of characters from the movie
      const characters = movie.characters;

      // Check if Wedge Antilles is in the characters array
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
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
