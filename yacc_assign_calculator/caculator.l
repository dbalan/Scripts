%{
#include <stdio.h>
#include "y.tab.h"

void yyerror(char *);
%}

digit [0-9]
operator [+-*]
whitespace [\t]
other .

%%
digit+ 
{
yyval = atoi(yytext);
return INT;
}

operator return *yytext;


whitespace ;

other {
yyerror(yytext);
}

%%
