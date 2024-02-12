#!/usr/bin/node

// Import the request and fs modules
const request = require('request');
const fs = require('fs');

// Get the URL and the file path from the arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL and pipe the response to the file
request(url).pipe(fs.createWriteStream(filePath, { encoding: 'utf8' }));
