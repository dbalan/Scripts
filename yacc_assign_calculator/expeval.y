%{
#include<stdio.h>
#include "lex.yy.c"

%}

%token VAR
%token IFL
%token IDE

%%

program:
program statement '\n' {printf("Valid Expression.\n",$2);}
    |
    ;

statement:
  IDE '=' expr';'
  | boolstatement
  | IFL '(' boolstatement ')' '{'statement '}'
  | statement ';' statement 
  | '{' statement '}'
  ;

boolstatement:
 expr '=''=' expr
 | expr '>''=' expr
 | expr '<''=' expr
 | IDE
 | VAR
 ;

expr:
  VAR
  | IDE         
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
