%{
#include <stdio.h>
#include <string.h>
#include <math.h>

int yylex(void);

int yyerror(const char *msg) {
    fprintf(stderr, "Error: %s\n", msg);
    return 0;
}

typedef struct {
    char name[32];
    int val;
} Variable;

Variable VariableList[1000];
int n = 0;

int findVariable(const char *name) {
    for (int i = 0; i < n; i++) {
        if (strcmp(name, VariableList[i].name) == 0) {
            return i;
        }
    }
    return -1;
}

void addVariable(const char *name) {
    strcpy(VariableList[n].name, name);
    n++;
}

int getValue(const char *name) {
    int index = findVariable(name);
    if (index != -1) {
        return VariableList[index].val;
    }
    return -9999;
}

int setValue(const char *name, int val) {
    int index = findVariable(name);
    if (index != -1) {
        VariableList[index].val = val;
        return 1;
    }
    return 0;
}

%}

%union {
    int intValue;
    char strValue[32];
}

%token <intValue> T_PRINT T_CONSTANT T_INT
%token <strValue> T_ID
%type <intValue> Expression
%left '+' '-'
%left '*' '/'
%right '^'
%nonassoc UMINUS

%%
Program     : Block;
Block       : '{' Slist '}' |
              '{' vardef Slist '}';
vardef      : T_INT varlist {};
varlist     : T_ID ',' varlist { addVariable($1); } | T_ID { addVariable($1); };
Slist       : Statement | Statement ';' Slist;
Statement   : T_PRINT '(' Expression ')' { printf("%d\n", $3); } |
              T_ID '=' Expression {
                  if (findVariable($1) == -1) {
                      fprintf(stderr, "Error: Variable '%s' is not declared.\n", $1);
                  } else {
                      setValue($1, $3);
                  }
              } |
              ;
Expression  : Expression '+' Expression { $$ = $1 + $3; } |
              Expression '-' Expression { $$ = $1 - $3; } |
              Expression '*' Expression { $$ = $1 * $3; } |
              Expression '/' Expression { $$ = $1 / $3; } |
              Expression '^' Expression { $$ = pow($1, $3); } |
              '-' Expression %prec UMINUS { $$ = -$2; } |
              '(' Expression ')' {} |
              T_CONSTANT { $$ = $1; } |
              T_ID {
                  int value = getValue($1);
                  if (value == -9999) {
                      fprintf(stderr, "Error: Variable '%s' is not declared.\n", $1);
                  }
                  $$ = value;
              };
%%

int main() {
    yyparse();
    return 0;
}
