<?php
    $options = array(
        PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8'
    );
    $db = new PDO('mysql:host=localhost;dbname=db', 'user', 'pw', $options);

?>

<html>
    <head>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet">
        <link href="style.css" rel="stylesheet">
        <meta charset="utf-8">
    </head>
    <body>
        <table class="table table-bordered table-striped table-hover">
            <thead class="thead-dark">
                <tr>
                    <th scope="col"></th>
                    <th scope="col" class="text-center">Est en</th>
                    <th colspan="6" class="text-center">A ramené</th>
                    <th colspan="2" class="text-center">A lavé</th>
                </tr>
                <tr>
                    <th scope="col">Pseudo</th>
                    <th scope="col">Retard</th>
                    <th scope="col">Riz</th>
                    <th scope="col">Café Senseo</th>
                    <th scope="col">Café filtre</th>
                    <th scope="col">Thé</th>
                    <th scope="col">Éponge</th>
                    <th scope="col">Liquide Vaiselle</th>
                    <th scope="col">Torchons</th>
                    <th scope="col">Micro ondes</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach($db->query('SELECT * from users') as $row) { ?>
                    <tr>
                        <th scope="row"><?php echo $row[0]; ?></th>
                        <td><?php echo $row[1]; ?></td>
                        <td><?php echo $row[2]; ?></td>
                        <td><?php echo $row[3]; ?></td>
                        <td><?php echo $row[4]; ?></td>
                        <td><?php echo $row[5]; ?></td>
                        <td><?php echo $row[6]; ?></td>
                        <td><?php echo $row[7]; ?></td>
                        <td><?php echo $row[8]; ?></td>
                        <td><?php echo $row[9]; ?></td>
                    </tr>
                <?php } ?>
            </tbody>
        </table>
    </body>
</html>