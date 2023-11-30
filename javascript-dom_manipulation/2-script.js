#!/usr/bin/node
/*
JavaScript modification du header au click sur l'id red_header ce qui passe le css de celui-ci en
text rouge
*/
const $JQ = window.$;
$JQ('#red_header').click(() => {
    $JQ('header').css({
	color: '#FF0000'
    });
});
