#!F:\xampp\perl\bin\perl.exe
use strict;
use warnings;

use CGI qw(:standard);

my $bananaAmount = param("banana");
my $appleAmount = param("apple");
my $amount = $bananaAmount + $appleAmount;

print header;

print start_html("Kasse");
print h2("Die Anzahl der Artikel ist: $amount");
print end_html;
