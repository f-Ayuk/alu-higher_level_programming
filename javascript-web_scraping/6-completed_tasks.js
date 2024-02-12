#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

// Make a GET request to the API
request(apiUrl, (err, res, body) => {
  // If an error occurred, handle it
  if (err) {
    console.error(err);
  } else {
    // Otherwise, parse the JSON data from the body
    const data = JSON.parse(body);

    // Initialize an empty object to store the results
    const results = {};

    // Loop through the data array
    for (let task of data) {
      // Get the user id and the completed status from the task
      const userId = task.userId;
      const completed = task.completed;

      // If the task is completed, increment the count for the user id
      if (completed) {
        // If the user id is not in the results object, initialize it to zero
        if (!results[userId]) {
          results[userId] = 0;
        }

        // Increment the count for the user id
        results[userId]++;
      }
    }

    // Print the results object
    console.log(results);
  }
});
