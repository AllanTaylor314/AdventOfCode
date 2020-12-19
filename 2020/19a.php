<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("19.txt");
$inputs=explode("\n\n",$input);
$rules=explode("\n",$inputs[0]);
$messages=explode("\n",$inputs[1],-1);
$count=0;
foreach ($rules as $r) {
	$tmp=explode(": ",$r);
	$rule_array[(int)$tmp[0]]=explode(" ",$tmp[1]);
}
//$message_flip=array_flip($messages);
//$valid_messages=[];
/*foreach (get_valid_messages_from_rule($rule_array[0]) as $valid) {
	//$valid_messages[]=$valid;
	if (isset($message_flip[$valid])) {$count++;}
}
var_dump($valid_messages);
*/
$regex=create_regex_from_id(0);
//echo $regex."\n";
foreach ($messages as $m) {
	if (preg_match('/^'.$regex.'$/',$m)) {$count++; echo "$m\n";}
}
echo "$count\n";

function create_regex_from_id($rule_id) {
	//echo "\n$rule_id";
	$rule=$GLOBALS['rule_array'][$rule_id];
	if ($rule[0][0]=='"') {
		return $rule[0][1];
	}
	/*if (in_array("|",$rule)) {
		foreach ($rule as $new_id) {
			// code...
		}
		return "(".create_regex_from_id($rule[0]).create_regex_from_id($rule[1])."|".create_regex_from_id($rule[3]).create_regex_from_id($rule[4]).")";
	}*/
	$out="(";
	foreach ($rule as $new_id) {
		$out=$out.($new_id=="|"?"|":create_regex_from_id($new_id));
	}
	return $out.")";
}
//Answer:
?>
