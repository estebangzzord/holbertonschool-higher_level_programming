#!/usr/bin/node
/*
Script JavaScript qui récupère le nom du personnage
depuis cette URL: https://swapi-api.hbtn.io/api/people/5/?format=json
*/
const $JQ = window.$;
$JQ.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (dataPeople) => {
    $JQ('#character').text(dataPeople.name);
});
