<?php
//error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("22.txt");
$inputs=explode("\n\n",$input."\n",-1);
$p1=explode("\n",$inputs[0]);
$p2=explode("\n",$inputs[1]);
array_shift($p1);
array_shift($p2);
$game_result=play_combat($p1,$p2);
if ($game_result[0]) {$winner=$game_result[1];}
else {$winner=$game_result[2];}
$winner[]=0;
$answer=0;
$winner=array_reverse($winner);
var_dump($winner);
foreach ($winner as $key => $value) {
	$answer+=($key*$value);
}
echo "$answer\n";

function play_combat($deck1,$deck2,$game=1) {
	//echo "$game\n";
	$hands_in_this_game=[];
	while (true) {
		$hand=implode(",",$deck1).";".implode(",",$deck2);
		//echo "$game: $hand\n";
		if (in_array($hand,$hands_in_this_game)) {
			return [true,$deck1,$deck2]; //Player 1 won
		} else {
			$hands_in_this_game[]=$hand;
		}
		if (count($deck1)==0) {return [false,$deck1,$deck2];} //Player 2 won
		if (count($deck2)==0) {return [true,$deck1,$deck2];} //Player 1 won
		$c1=array_shift($deck1);
		$c2=array_shift($deck2);
		if ($c1<=count($deck1) && $c2<=count($deck2)) {
			if(play_combat(array_slice($deck1,0,$c1),array_slice($deck2,0,$c2),$game+1)[0]) {
				array_push($deck1,$c1,$c2);
			} else {
				array_push($deck2,$c2,$c1);
			}
		} else {
			if($c1>$c2) {
				array_push($deck1,$c1,$c2);
			} else {
				array_push($deck2,$c2,$c1);
			}
		}
	}
}
//Answer:
?>
