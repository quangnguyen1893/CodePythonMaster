%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int column_number = 1; // Thêm biến để theo dõi số thứ tự của cột
int row_number = 1; // Thêm biến để theo dõi số thứ tự của hàng

void printResult(int col, int val) { // Thêm tham số row
    if (val != 0) {
        printf("%d:%d ", col, val); // Cập nhật công thức tính số cột
    }
}
int yylex();
int yyerror(const char *msg) {
	fprintf(stderr, "Error at line: %s\n", msg);
	exit(1);
}
%}

%token T_CONSTANT T_UMINUS T_ENDL
%nonassoc UMINUS
%%

matrix: rows;
rows:   rows row | row; //một ma trận có thể có nhiều hàng
row:    value | value T_ENDL{ //mỗi một hàng có thể có 1 cột hoặc nhiều cột
            printf("\n");
            row_number ++;
            column_number = 1;//reset chi so cot ve mac dinh
        };
value:  T_CONSTANT{$$ = $1; printResult(column_number, $1);column_number++;} |  //cập nhật giá trị
        '-' T_CONSTANT  %prec UMINUS{$$ = $2;printResult(column_number, -$2);column_number++;};//chấp nhận giá trị số âm
%%

int main() {
    yyparse();
    printf("\n");
    return 0;
}
