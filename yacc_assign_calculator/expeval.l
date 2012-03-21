
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

0 { return VAR; }
{digitn}{digit}* {return VAR; }

{letter}+{digit}* {return VAR; }
{operand} return *yytext;
{white} ;

{other} yyerror("invalid character");
%%

;int yywrap(void){
;return 1;
;}

