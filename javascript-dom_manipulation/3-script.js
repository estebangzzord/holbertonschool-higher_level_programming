#!/usr/bin/node
/*
JavaScript Ajout  de la classe red au click sur red_header au header
*/
const $JQ = window.$;
$JQ('#red_header').click(function () {
    $JQ('header').addClass('red');
});
