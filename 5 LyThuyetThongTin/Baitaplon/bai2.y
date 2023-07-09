%{
#include <stdio.h>
#include <string.h>
int yylex (void);
int yyerror(const char *msg) {
	fprintf(stderr, "Error:%s\n", msg);
	return 0;
}

typedef struct {
	char name[32];
	int val;
} Variable;

Variable VariableList[1000];

int n = 0;

int findVariable(const char *name) {
	for (int i=0; i<n; i++) {
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
	for (int i=0; i<n; i++) {
		if (strcmp(name, VariableList[i].name) == 0) {
			return VariableList[i].val;
		}
	}
	return -1;
}

int setValue(const char *name, int val) {
	for (int i=0; i<n; i++) {
		if (strcmp(name, VariableList[i].name) == 0) {
			VariableList[i].val = val;
			return 1;
		}
	}
	return 0;
}

void printVariable() {
	for (int i=0; i<n; i++) {
		printf("%s %d\n", VariableList[i].name, VariableList[i].val);
	}
}

%}

%union {
	int intValue;
	char strValue[32];
}

%token <intValue> T_PRINT T_CONSTANT T_INT
%token <strValue> T_ID
%type <intValue> Expression
%left	'+' '-'
%left	'*' '/'
%nonassoc UMINUS

%%
Program		: Block;
Block		: '{' Slist '}' |
			'{' vardef Slist '}';
vardef		: T_INT varlist {};
varlist		: T_ID ',' varlist {addVariable($1);} | T_ID {addVariable($1);};
Slist		: Statement | Statement ';' Slist;
Statement	: T_PRINT '(' Expression ')' {/*printVariable();*/printf("PRINT\n");} |
			T_ID '=' Expression {setValue($1,$3);printf("TO %s\n",$1);} | ;
Expression	: Expression '+' Expression {$$ = $1 + $3;printf("ADD\n");} |
			Expression '-' Expression {$$ = $1 - $3;printf("SUB\n");} |
			Expression '*' Expression {$$ = $1 * $3;printf("MUL\n");} |
			Expression '/' Expression {$$ = $1 / $3;printf("DIV\n");} |
			'-' Expression %prec UMINUS {$$ = - $2;printf("UMINUS\n");} |
			'(' Expression ')' {} |			
			T_CONSTANT {$$ = $1;printf("PUSH %d\n", $1);} |
			T_ID {$$=getValue($1);printf("VARIABLE %s\n", $1);};
%%

int main() {
	yyparse();
	return 0;
}