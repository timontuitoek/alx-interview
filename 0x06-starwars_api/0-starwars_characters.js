#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Defining the base URL for the Star Wars API
const API_URL = 'https://swapi-api.hbtn.io/api';

// Checking if command line arguments are provided
if (process.argv.length > 2) {
  // Making a GET request to the specified film endpoint
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    // Handling any errors that occur during the request
    if (err) {
      console.log(err);
    }
    // Parsing the response body to extract character URLs
    const charactersURL = JSON.parse(body).characters;

    // Mapping each character URL to a Promise to fetch their names asynchronously
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        // Making a GET request to the character URL
        request(url, (promiseErr, __, charactersReqBody) => {
          // Handling any errors that occur during the request
          if (promiseErr) {
            reject(promiseErr);
          }
          // Parsing the response body to extract the character's name
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    // Resolving all character name Promises concurrently
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n'))) // Logging all character names
      .catch(allErr => console.log(allErr)); // Handling any errors that occur during Promise resolution
  });
}
