<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("13.txt");
$inputs=explode("\n",$input,-1);
$timestamp=$inputs[0];
$buses=explode(",",$inputs[1]);
$bestwait=10000;
foreach ($buses as $bus) {
	if ($bus=="x") {continue;}
	$wait=$bus-($timestamp%(int)$bus);
	if ($wait<$bestwait) {
		$bestwait=$wait;
		$bestid=$bus;
	}
	echo $bus." time:".$wait."\n";
}
echo ($bestid*$bestwait)." id:$bestid ($bestwait min)\n";
//Answer:
?>
