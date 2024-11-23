#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command-line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// API URL for the given movie ID
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch movie details
request(filmUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Fetch each character's name in order
  fetchCharacters(characterUrls);
});

// Function to fetch character names
function fetchCharacters(urls) {
  const names = [];

  const fetchCharacter = (index) => {
    if (index >= urls.length) {
      // All names fetched, print them
      names.forEach(name => console.log(name));
      return;
    }

    request(urls[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to fetch data: ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      names.push(character.name);

      // Fetch the next character
      fetchCharacter(index + 1);
    });
  };

  fetchCharacter(0); // Start with the first character
}
