#!/usr/bin/node
/*
JavaScript met à jour le contenu du header au click sur l'id update_header
*/
const $JQ = window.$;
$JQ('#update_header').click(() => {
    $JQ('header').html('New Header!!!');
});
