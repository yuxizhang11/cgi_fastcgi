#!F:\xampp\perl\bin\perl.exe
use strict;
use warnings;

use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
print "Content-type: text/html\n\n";

my $user = param('username');
my $item = param('item');
my $qty = param('quantity');
my $price = param('price');

my $subtotal = $qty * $price;
my $tax = $subtotal * 0.19;
my $total = $subtotal + $tax;

print "<head>
    <meta charset=\"UTF-8\">
    <title>Online Shop</title>
</head>";
print "<h2>The Shop</h2>";
print "Hier ist Ihre Bestellung: <br />";
print "Produkt: $item, Stückpreis: $price€, Anzahl: $qty <br />";
print "Zwischensumme: $subtotal€ <br />";
printf "Mehrwertsteuern: %.2f€ <br />", $tax;
printf "Gesamtsumme: %.2f€ <br />", $total;
print "Danke für Ihren Einkauf, $user."