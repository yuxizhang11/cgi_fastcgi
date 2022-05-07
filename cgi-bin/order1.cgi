#!F:\xampp\perl\bin\perl.exe
use strict;
use warnings;

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);

my $counter = cookie('counter') || 0;
$counter++;

my $cookie = cookie(
    -name => "counter",
    -value => $counter,
    -expires => "+1m"
);

print "Content-Type: text/html\nSet-Cookie: $cookie\n\n";


print << "END_HTML";
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Shop</title>
    <style>
    body{
    height: 100%;
}
.Seite{
    display: grid;
    grid-template-columns: 80% 20%;
}
td, th{
    border: 1px solid black;
    border-collapse: collapse;
}
.Tabelle{
    height: 200px;
    width: 100%;
    text-align: center;
    vertical-align: middle;
    border-collapse: collapse;
}
.Warenkorbkopf{
    margin-left: 10px;
}
</style>
</head>
<body>
    <h1>Der Shop</h1>
    <form action="/cgi-bin/order1.cgi" method="post">
        <div class="Seite">
            <table class="Tabelle">
                <thead>
                <tr>
                    <th>Produkt 1</th>
                    <th>Produkt 2</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td><img src="../img/banana.png" width="150" height="75"></td>
                    <td><img src="../img/apple.jpg" width="125" height="125"></td>
                </tr>
                <tr>
                    <td><input type="submit" value="Zum Warenkob hinzufügen"></td>
                    <td><input type="submit" value="Zum Warenkob hinzufügen"></td>
                </tr>
                </tbody>
            </table>
            <div class="Warenkorbkopf">
                Warenkorb: $counter
            </div>
        </div>
    </form>
</body>
</html>

END_HTML
