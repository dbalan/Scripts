%{
#include<stdio.h>
#include "lex.yy.c"

%}

%token INTEGER

%%

program:
program expr '\n' {printf("Out:%d\n",$2);}
    |
    ;
expr:
  INTEGER         {$$=$1;}
  | expr '+' expr {$$=$1+$3;}
  | expr '-' expr {$$=$1-$3;}
  | expr '*' expr {$$=$1*$3;}
  | expr '/' expr {$$=$1/$3;}
  ;
%%
     
int main(void){
  return yyparse();
}


int yyerror()
{
  printf("\nError ");
  return 1;
}
