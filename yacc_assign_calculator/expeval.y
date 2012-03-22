%{
#include<stdio.h>
#include "lex.yy.c"

%}

%token VAR
%token IFL
%token AVAR

%%

program:
program statement '\n' {printf("Valid Expression.\n",$2);}
    |
    ;

statement:
   AVAR
  |AVAR '=' expr
  | boolstatement
  | IFL '(' statement ')' '{' statement '}'
  | statement ';' statement
  | '{' statement '}'
  ;

boolstatement:
 expr '=''=' expr
 | expr '>''=' expr
 | expr '<''=' expr
 ;

expr:
  VAR
  | AVAR         
  | expr '+' expr 
  | expr '-' expr 
  | expr '*' expr 
  | expr '/' expr 
  | '(' expr ')'
  |
  ;
%%
     
int main(void){
  return yyparse();
}


int yyerror()
{
  printf("\nInvalid Expression!!\n");
  //exit(0);
}
