%{
#include<stdio.h>
#include "lex.yy.c"

%}

%token VAR

%%

program:
program expr '\n' {printf("Valid Expression.\n",$2);}
    |
    ;
expr:
  VAR         
  | expr '+' expr 
  | expr '-' expr 
  | expr '*' expr 
  | expr '/' expr 
| '(' expr ')'  
  ;
%%
     
int main(void){
  return yyparse();
}


int yyerror()
{
  printf("\nInvalid Expression!!\n");
  exit(0);
}
