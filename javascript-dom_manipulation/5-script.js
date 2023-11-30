#!/usr/bin/node
/*
JavaScript ajoute une instance <li>Item</li> à chaque click sur l'id add_item
*/
const $JQ = window.$;
$JQ('#add_item').click(() => {
    $JQ('.my_list').append('<li>Item</li>');
});
