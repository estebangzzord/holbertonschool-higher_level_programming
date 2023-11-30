#!/usr/bin/node
/*
JavaScript Altern successivement les classes green et red au click sur l'id toggle_header
*/
const $JQ = window.$;
$JQ('#toggle_header').click(() => {
    $JQ('header').toggleClass('green');
    $JQ('header').toggleClass('red');
});
