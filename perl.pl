#!/usr/bin/perl

use strict;
use warnings;


# Get the number of elements from a list
my @list = (0, 1, 2, 3);
my $num_elements = @list;
assert(4, $num_elements);


# Normalizing booleans
use constant { true => 1, false => 0 }; # There is no true or false in perl
my $false_non_boolean = '';
my $true_non_boolean = 'Hi';
assert(false, !!$false_non_boolean);
assert(true, !!$true_non_boolean);


sub assert {
    my $expected_value = shift;
    my $expression_result = shift;

    if ($expected_value != $expression_result) {
        print 'Assertion Error!';
    }
}
