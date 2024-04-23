#!/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    
    request(url, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
            return;
        }
        
        if (response.statusCode !== 200) {
            console.error('Status Code:', response.statusCode);
            return;
        }
        
        const filmData = JSON.parse(body);
        const characters = filmData.characters;
        
        characters.forEach(characterUrl => {
            request(characterUrl, (error, response, body) => {
                if (error) {
                    console.error('Error:', error);
                    return;
                }
                
                if (response.statusCode !== 200) {
                    console.error('Status Code:', response.statusCode);
                    return;
                }
                
                const characterData = JSON.parse(body);
                console.log(characterData.name);
            });
        });
    });
}

function main() {
    if (process.argv.length !== 3) {
        console.log("Usage: node script_name.js movie_id");
        return;
    }
    
    const movieId = process.argv[2];
    getMovieCharacters(movieId);
}

if (require.main === module) {
    main();
}
