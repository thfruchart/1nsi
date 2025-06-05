<!doctype html>
<html>
 <head>
     <title>
        Résultat du calcul
     </title>
     <meta charset="utf8">
 </head>
 <body>
<p> Vous avez saisi la valeur : 
    <?php
    if (isset($_GET['n']))
    {
        $n = $_GET['n'];
        
        echo $n;

    }
    else { echo "Erreur";}
    ?>
</p>

 </body>
</html>
