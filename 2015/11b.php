<?php
error_reporting(E_ERROR | E_PARSE);
function check_password_valid($password) {
	return
		preg_match('/^[^iol]*$/',$password) &&
		preg_match('/(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)/',$password) &&
		preg_match('/(.)\1.*(.)\2/',$password);
}
//optimizations:
//replace iol with next letter up (jpm)
$input="hxbxxyzz";//file_get_contents("11t.txt");
$input++;
while (!check_password_valid($input)) {
	$input++;
	echo "\r".$input;
}
echo "\r".$input."\n";
//Answer: hxcaabcc
?>
