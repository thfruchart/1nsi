<!DOCTYPE html>
<html>
<body>
<table border=1>
<tr> <td> x </td>

<?php
for($j = 1; $j <= 10; $j++)
   { echo "<td><b> $j </b> </td>";}
?>
</tr>

<?php
for($i=1;$i<=10;$i++ )
{
    echo "<tr> <td><b> $i </b></td>";
    
    echo "</tr>
    ";
}
?>  
</table>
</body>
</html>
