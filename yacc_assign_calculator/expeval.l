
%{
#include "y.tab.h"



%}
digit [0-9]
digitn [1-9]
operand [-+*/\n\)\(\;{}=]
white [\t]
letter [a-z]
other .
%%
if {return IFL;}
0 { return VAR; }
{digitn}{digit}* {return VAR; }

{letter}+{digit}* {return AVAR; }
{operand} return *yytext;
{white} ;

{other} yyerror("invalid character");
%%

;int yywrap(void){
;return 1;
;}

