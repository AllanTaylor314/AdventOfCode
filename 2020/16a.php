<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("16.txt");
$inputs=explode("\n\n",$input."\n",-1);
$ticket_rules=explode("\n",$inputs[0]);
$ticket_mine=explode("\n",$inputs[1])[1];
$ticket_nearby=explode("\n",$inputs[2],-1);
array_shift($ticket_nearby);
$scan_error=0;
$ticket_rules_array=[];
foreach ($ticket_nearby as $k => $t) {
	$ticket_nearby_array[$k]=explode(",",$t);
}
foreach ($ticket_rules as $key => $rule) {
	$tmp=explode(": ",$rule);
	$ranges=explode(" ",$tmp[1]);
	$ra=explode("-",$ranges[0]);
	$rb=explode("-",$ranges[2]);
	$mina=$ra[0];
	$maxa=$ra[1];
	$minb=$rb[0];
	$maxb=$rb[1];
	var_dump($rb);
	for ($value=$mina; $value<=$maxb; $value++) {
		if ($value>$maxa && $value<$minb) {continue;}
		//$ticket_rules_array[$tmp[0]][$value]=true;
		$ticket_rules_array[$value]=true; //is the number valid anywhere
	}
}
foreach ($ticket_nearby_array as $nearby) {
	foreach ($nearby as $field_val) {
		//if (!$ticket_rules_array) {$invalid++; break;}
		if (!isset($ticket_rules_array[$field_val])) {$scan_error+=$field_val;}
	}
}
var_dump($ticket_rules);
var_dump($ticket_mine);
var_dump($ticket_nearby);
echo "$scan_error\n";
//Answer:
?>
