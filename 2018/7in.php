<?php
//header('Content-Type: text/plain)';
$input = ' can begin.
Step P must be finished before step G can begin.
Step X must be finished before step V can begin.
Step H must be finished before step R can begin.
Step O must be finished before step W can begin.
Step C must be finished before step F can begin.
Step U must be finished before step M can begin.
Step E must be finished before step W can begin.
Step F must be finished before step J can begin.
Step W must be finished before step K can begin.
Step R must be finished before step M can begin.
Step I must be finished before step K can begin.
Step D must be finished before step B can begin.
Step Z must be finished before step A can begin.
Step A must be finished before step N can begin.
Step T must be finished before step J can begin.
Step B must be finished before step N can begin.
Step Y must be finished before step M can begin.
Step Q must be finished before step N can begin.
Step G must be finished before step V can begin.
Step J must be finished before step N can begin.
Step M must be finished before step V can begin.
Step N must be finished before step V can begin.
Step K must be finished before step S can begin.
Step V must be finished before step L can begin.
Step S must be finished before step L can begin.
Step W must be finished before step D can begin.
Step A must be finished before step V can begin.
Step T must be finished before step Y can begin.
Step H must be finished before step W can begin.
Step O must be finished before step C can begin.
Step P must be finished before step S can begin.
Step Z must be finished before step N can begin.
Step G must be finished before step K can begin.
Step I must be finished before step T can begin.
Step D must be finished before step M can begin.
Step A must be finished before step Q can begin.
Step O must be finished before step S can begin.
Step N must be finished before step L can begin.
Step V must be finished before step S can begin.
Step M must be finished before step N can begin.
Step A must be finished before step B can begin.
Step H must be finished before step B can begin.
Step H must be finished before step G can begin.
Step Q must be finished before step M can begin.
Step U must be finished before step E can begin.
Step C must be finished before step S can begin.
Step M must be finished before step L can begin.
Step T must be finished before step L can begin.
Step I must be finished before step N can begin.
Step Y must be finished before step N can begin.
Step K must be finished before step V can begin.
Step U must be finished before step B can begin.
Step H must be finished before step Z can begin.
Step H must be finished before step Y can begin.
Step E must be finished before step F can begin.
Step F must be finished before step Q can begin.
Step R must be finished before step G can begin.
Step T must be finished before step S can begin.
Step T must be finished before step Q can begin.
Step X must be finished before step H can begin.
Step Q must be finished before step S can begin.
Step Q must be finished before step J can begin.
Step G must be finished before step S can begin.
Step D must be finished before step S can begin.
Step A must be finished before step J can begin.
Step I must be finished before step Y can begin.
Step U must be finished before step K can begin.
Step P must be finished before step R can begin.
Step A must be finished before step T can begin.
Step J must be finished before step K can begin.
Step Z must be finished before step J can begin.
Step Z must be finished before step V can begin.
Step P must be finished before step X can begin.
Step E must be finished before step I can begin.
Step G must be finished before step L can begin.
Step G must be finished before step N can begin.
Step J must be finished before step L can begin.
Step I must be finished before step Q can begin.
Step Q must be finished before step K can begin.
Step B must be finished before step J can begin.
Step R must be finished before step T can begin.
Step Z must be finished before step K can begin.
Step J must be finished before step V can begin.
Step R must be finished before step L can begin.
Step R must be finished before step N can begin.
Step W must be finished before step Q can begin.
Step U must be finished before step W can begin.
Step Y must be finished before step V can begin.
Step C must be finished before step T can begin.
Step X must be finished before step B can begin.
Step M must be finished before step S can begin.
Step B must be finished before step K can begin.
Step D must be finished before step N can begin.
Step P must be finished before step U can begin.
Step N must be finished before step K can begin.
Step M must be finished before step K can begin.
Step C must be finished before step A can begin.
Step W must be finished before step B can begin.
Step C must be finished before step Y can begin.
Step T must be finished before step V can begin.
Step W must be finished before step M can begin.
Step ';
$inputs = explode(' can begin.
Step ', $input);
$n = 0;
foreach ($inputs as $i) {
	if (strlen($i) > 20) {
		$theArray[$n] = explode(' must be finished before step ', $i);
		$n++;
	}
}