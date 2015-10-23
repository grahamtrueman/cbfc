#!/bin/perl


require("/RSCentral/Pearl-Web/library.pl") ;

&initialise_pw;

$HTMLdir        = '/export/cbfc/static/HTML/'          ;

$DB             = 'DBI:mysql:cbfc'                     ;
$DBusername     = 'root'                               ;
$DBpassword     = 'RomantiC'                           ;

$DEBUGlevel     = 10                                   ;


print "content-type: text/html\n\n" ;

&$sub_read_input ;
&$sub_loadFragments($HTMLdir.'main.html')             ;   #   get starting fragments
&$sub_read_input                                       ;   #   read input parameters

&$sub_write_output ;

