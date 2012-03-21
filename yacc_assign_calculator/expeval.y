%{
#include<stdio.h>
#include "lex.yy.c"

%}

%token INTEGER

%%

program:
program expr '\n' {printf("Valid Expression.\n",$2);}
    |
    ;
expr:
  INTEGER         {$$=$1;}
  | expr '+' expr {$$=$1+$3;}
  | expr '-' expr {$$=$1-$3;}
  | expr '*' expr {$$=$1*$3;}
  | expr '/' expr {$$=$1/$3;}
| '(' expr ')' {}  
  ;
%%
     
int main(void){
  return yyparse();
}


int yyerror()
{
  printf("\nInvalid Expression!!\n");
  return 1;
}
