%{
#include <stdio.h>
#include <string.h>
#include <math.h>

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

/*Kiểm tra biến đã có trong danh sách chưa, nếu chưa trả về -1*/
int findVariable(const char *name) {
	for (int i=0; i<n; i++) {
		if (strcmp(name, VariableList[i].name) == 0) {
			return i;
		}
	}
	return -1;
}

void addVariable(const char *name) {
	/*Thêm biến tên name vào danh sách VariableList*/
	strcpy(VariableList[n].name, name);
	n++;
}

int getValue(const char *name) {
	/*lấy giá trị của biến, nếu ko có thì trả về bằng giá trị 0*/
	for (int i=0; i<n; i++) {
		if (strcmp(name, VariableList[i].name) == 0) {
			return VariableList[i].val;
		}
	}
	return -1;
}

int setValue(const char *name, int val) {
	/*Gán val vào biến tên name*/
	for (int i=0; i<n; i++) {
		if (strcmp(name, VariableList[i].name) == 0) {
			VariableList[i].val = val;
			return 1;
		}
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
%left	'+' '-'
%left	'*' '/'
%right	'^'
%nonassoc UMINUS

%%
Program		: Block;
Block		: '{' Slist '}' |
			'{' vardef Slist '}';
vardef		: T_INT varlist {};
varlist		: T_ID ',' varlist {addVariable($1);} | T_ID {addVariable($1);};
Slist		: Statement | Statement ';' Slist;
Statement	: T_PRINT '(' Expression ')' {printf("%d\n", $3);} |
			T_ID '=' Expression {setValue($1,$3);} | ;
Expression	: Expression '+' Expression {$$ = $1 + $3;} |
			Expression '-' Expression {$$ = $1 - $3;} |
			Expression '*' Expression {$$ = $1 * $3;} |
			Expression '/' Expression {$$ = $1 / $3;} |
			Expression '^' Expression {$$ = pow($1,$3);} |
			'-' Expression %prec UMINUS {$$ = - $2;} |
			'(' Expression ')' {} |			
			T_CONSTANT {$$ = $1;} |
			T_ID {$$ = getValue($1);};
%%

int main() {
	yyparse();
	return 0;
}