
%{
#include "y.tab.h"



%}
digit [0-9]
operand [-+*/\n]
white [\t]
other .
%%
{digit}+ { yylval=atoi(yytext); return INTEGER; }

{operand} return *yytext;
{white} ;

{other} yyerror("invalid character");
%%
int yywrap(void){
return 1;
}

