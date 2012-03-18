
%{
#include "y.tab.h"
%}

digit [0-9]
operand [-+*/]
whitespace [\t]
other . 

%%
{digit}+
{ yylval=atoi(yytext);
  return INTEGER;
}

{operand} return *yytext;
{whitespace} ; /* skip */

{other} yyerror("invalid character");

%%

int yywrap(void){
/* Done, were good! */
return 1;

}

