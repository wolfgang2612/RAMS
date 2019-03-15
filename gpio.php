<?php
if (isset ( $_GET["pic"] )) {
	$pic = strip_tags ($_GET["pic"]);
	if ( (is_numeric($pic)) && ($pic <= 7) && ($pic >= 7) ) {
		
		system("gpio mode ".$pic." out");
		exec ("gpio read ".$pic, $status, $return );
		if ($status[0] == "0" ) { $status[0] = "1"; }
		else if ($status[0] == "1" ) { $status[0] = "0"; }
		system("gpio write ".$pic." ".$status[0] );
		exec ("gpio read ".$pic, $status, $return );
		echo($status[0]);
		
	}
	else { echo ("fail"); }
} 
else { echo ("fail"); }
?>
