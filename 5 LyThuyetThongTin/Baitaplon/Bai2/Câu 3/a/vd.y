%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define atoa(x)
int row = 1;
int col = 1;
void printValue(int val){
	if (val != 0) {
		printf("%d:%d ", col, val);
	}
col++;
}
void toNextLine(){
	printf("\n");
	row++;
	col = 1;
}
int yyerror(const char *msg) {
	fprintf(stderr, "Error:%s\n", msg);
	return 0;
}
// Hàm kiểm tra lỗi
int yylex();
%}

%token T_CONSTANT T_UMINUS T_ENDL

%%

Rows : Row Rows | { printf("\n");} ;
Row : int | endl ;
int : T_CONSTANT { $$ = $1;
		printValue($1); } |
		T_UMINUS T_CONSTANT { $$ = -$2;
		printValue(-$2);
		} ;
endl : T_ENDL { toNextLine(); } ;
%%
int main() {
	yyparse();
	return 0;
}