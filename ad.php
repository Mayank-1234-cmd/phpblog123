<?php

$input = array("ad1", "ad2", "ad3", "ad4", "ad5");
$rand_keys = array_rand($input, 1);
echo "Toastify({
  text: '".$input[$rand_keys[0]]."',
  offset: {
    x: 50, // horizontal axis - can be a number or a string indicating unity. eg: '2em'
    y: 10 // vertical axis - can be a number or a string indicating unity. eg: '2em'
  },
}).showToast();"

?>