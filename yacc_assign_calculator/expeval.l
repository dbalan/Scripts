
%{
#include "y.tab.h"



%}
digit [0-9]
digitn [1-9]
operand [-+*/\n\)\(]
white [\t]
letter [a-z]
other .
%%

0 { yylval=atoi(yytext); return INTEGER; }
{digitn}{digit}* { yylval=atoi(yytext); return INTEGER; }

{letter}+{digit}* { yylval=atoi(yytext); return INTEGER; }
{operand} return *yytext;
{white} ;

{other} yyerror("invalid character");
%%
int yywrap(void){
return 1;
}

