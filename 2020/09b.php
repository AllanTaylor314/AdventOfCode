<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("9.txt");
$inputs=explode("\n",$input,-1);
$find=22406676;
$pre=25;
foreach ($inputs as $key => $i) {
	$acc=$i;
	$keyn=$key;
	$range=[$i];
	while ($acc<$find) {
		$keyn++;
		$range[]=$inputs[$keyn];
		$acc+=$inputs[$keyn];
	}
	if ($acc==$find) {
		//var_dump($range);
		echo "min: ".min($range).", max: ".max($range).", sum: ".(min($range)+max($range))."\n";
		exit();
	}
}
echo "\n";
//Answer:
?>
