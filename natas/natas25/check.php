<?php
$filename = "....//....//....//....//....//etc/".passthru("ls /etc | grep rc.");
$filename = urlencode($filename);
if(strstr($filename,"../")){
    $filename=str_replace("../","",$filename);
}
$filepath = 'doc/'.$filename;
echo $filepath."\n";
include($filepath);
?>
