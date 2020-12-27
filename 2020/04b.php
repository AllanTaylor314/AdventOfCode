<?php
error_reporting(E_ERROR | E_PARSE);
$input=file_get_contents("4.txt");
$inputs=explode("\n\n",$input);
$n=0;
$passport=[];

function validate_passport($pass) {
	var_dump($pass);
	if ((int)$pass['byr']<1920 || (int)$pass['byr']>2002) {
		//echo "Err:byr\n";
		return false;
	}
	if ((int)$pass['iyr']<2010 || (int)$pass['iyr']>2020) {
		//echo "Err:iyr\n";
		return false;
	}
	if ((int)$pass['eyr']<2020 || (int)$pass['eyr']>2030) {
		//echo "Err:eyr\n";
		return false;
	}
	//var_dump($pass['hgt']);
	if (preg_match('/[0-9]+(in|cm)$/',$pass['hgt'],$re)) {
		//echo $re[1];
		if (($re[1]=="cm" && ((int)$pass['hgt']<150 || (int)$pass['hgt']>193)) ||
		($re[1]=="in" && ((int)$pass['hgt']<59 || (int)$pass['hgt']>76))) {
			//echo "Err:hgt - rng\n";
			return false;
		}
	} else {
		//echo "Err:hgt - fmt\n";
		return false;
	}
	if (!preg_match('/^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$/',$pass['hcl'])) {
		//echo "Err:hcl\n";
		return false;
	}
	if (!preg_match('/^(amb|blu|brn|gry|grn|hzl|oth)$/',$pass['ecl'])) {
		//echo "Err:ecl\n";
		return false;
	}
	if (!preg_match('/^[0-9]{9}$/',$pass['pid'])) {
		//echo "Err:pid\n";
		return false;
	}
	//echo "200:OK\n";
	//var_dump($pass);
	return true;
}

foreach ($inputs as $i) {
	$temp=explode(" ",preg_replace("/\s+/"," ",$i));
	//var_dump($temp);
	foreach($temp as $key => $value) {
		$tmp=explode(":",str_replace(" ","",$value));
		$passport[$tmp[0]]=$tmp[1];
	}
	//var_dump($passport);
	if (preg_match('/byr:/',$i) &&
	preg_match('/iyr:/',$i) &&
	preg_match('/eyr:/',$i) &&
	preg_match('/hgt:/',$i) &&
	preg_match('/hcl:/',$i) &&
	preg_match('/ecl:/',$i) &&
	preg_match('/pid:/',$i) &&
	validate_passport($passport)) {
		//echo "^Valid^"."\n\n";
		$n++;
	} else {
		//echo "^Invalid^"."\n\n";
		//var_dump($passport);
	}
	/*if (preg_match('/byr:[1,2][0,9][0-9][0-9]/',$i) &&
	preg_match('/iyr:[1,2][0,9][0-9][0-9]/',$i) &&
	preg_match('/eyr:/',$i) &&
	preg_match('/hgt:/',$i) &&
	preg_match('/hcl:/',$i) &&
	preg_match('/ecl:/',$i) &&
	preg_match('/pid:/',$i)) {
		$n++;
	}*/
}
echo $n."\n";
//Answer:
?>
