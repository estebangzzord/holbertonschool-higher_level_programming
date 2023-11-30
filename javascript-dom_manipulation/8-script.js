#!/usr/bin/node
/*
Script JavaScript qui récupère et répertorie le titre de tous les films
en utilisant cette URL : https://swapi-api.hbtn.io/api/people/5/?format=json
*/

const $JQ = window.$;
$JQ(document).ready(() => {
    $JQ.get('https://swapi-api.hbtn.io/api/films/?format=json', (dataFilms) => {
	for (const movie in data.results) {
	    $JQ('#list_movies').append('<li>' + dataFilms.results[movie].title + '</li>');
	}
    });
});
