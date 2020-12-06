<?php
error_reporting(E_ERROR | E_PARSE);
function looksay($input) {
	$output="";
	$reps=0;
	$prevchar=$input[0];
	foreach (str_split($input) as $key => $char) {
		if ($char==$prevchar) {
			$reps++;
		} else {
			$output=$output.$reps.$prevchar;
			$prevchar=$char;
			$reps=1;
		}
	}
	$output=$output.$reps.$prevchar; //gotta get that last set
	return $output;
}
//$input_file=file_get_contents("10.txt");
$currentval="1113222113";
//$currentval="1";
for ($i=0;$i<40;$i++) {
	//echo $i." - ".$currentval."\n";
	$currentval=looksay($currentval);
}
//echo $i." - ".$currentval."\n";
echo strlen($currentval)."\n";
//echo looksay("1113222113")."\n";
//Answer: 252594
?>
