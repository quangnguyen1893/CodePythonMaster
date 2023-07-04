%{
#include <stdio.h>
int yylex();
int yyerror(char *msg) {
    fprintf(stderr, "Error: %s\n", msg);
    return 0;
};

%}

%token T_PRINT T_CONSTANT
%left '+' '-'
%left '*' '/'
%nonassoc UMINUS

%%

Program    : Block ;


Block             : '{' Slist '}' ;
Slist      : Statement |
             Statement ';' Slist ;

Statement  : T_PRINT '(' Expression ')' {printf("PRINT\n");} | ;

Expression : Expression '+' Expression {printf("ADD\n");} |
             Expression '-' Expression {printf("SUB\n");} |
             Expression '*' Expression {printf("MUL\n");} |
             Expression '/' Expression {printf("DIV\n");} |
             '-' Expression %prec UMINUS {printf("UMINUS\n");} |
             '(' Expression ')' {} |
             T_CONSTANT {printf("PUSH %d\n", $1);} ;
%%
int main() {
  yyparse();
  return 0;
}