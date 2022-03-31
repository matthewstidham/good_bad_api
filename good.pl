#!/usr/bin/perl

print("Hello world!\n");

use warnings;
use strict;
use JSON;
use Data::Dumper;

my $data_file = open(FH, '<', 'good_api.json') or die "good_api.json: $!";
print($data_file);
my $text = decode_json($data_file);

print Dumper($text);

close(FH);
