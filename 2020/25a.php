<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("25.txt");
$inputs=explode("\n",$input,-1);
$card_pub=5764801;//(int)$inputs[0];
$door_pub=17807724;//(int)$inputs[1];
$card_pub=(int)$inputs[0];
$door_pub=(int)$inputs[1];
$value=1;
$sub=7;
//$loop=10;
for ($i=0;true;++$i) {
	if ($value==$card_pub) {$card_loop=$i;break;}
	$value*=$sub;
	$value=$value%20201227;
//	echo "$value\n";
}
$value=1;
for ($i=0;true;++$i) {
	if ($value==$door_pub) {$door_loop=$i;break;}
	$value*=$sub;
	$value=$value%20201227;
//	echo "$value\n";
}
echo "Card:$card_loop\n";
echo "Door:$door_loop\n";
$sub=$door_pub;
$value=1;
for ($i=0;$i<$card_loop;++$i) {
	$value*=$sub;
	$value=$value%20201227;
//	echo "$value\n";
}
echo "Key: $value\n";
//Answer: 17032383
?>
