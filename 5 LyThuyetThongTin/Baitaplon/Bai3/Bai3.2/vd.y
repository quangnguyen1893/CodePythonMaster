%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int column_number = 1; // Thêm biến để theo dõi số thứ tự của cột
int row_number = 1; // Thêm biến để theo dõi số thứ tự của hàng

void print_td(int val){
    printf("<td>%d</td>", val);
};
int yylex();
int yyerror(const char *msg) {
	fprintf(stderr, "Error at line: %s\n", msg);
	exit(1);
}
%}

%token T_CONSTANT T_UMINUS T_ENDL
%nonassoc UMINUS
%%

rows:   rows row | row; //một ma trận có thể có nhiều hàng
row:    value | value T_ENDL{ //mỗi một hàng có thể có 1 cột hoặc nhiều cột
            printf("</tr>\n");
            printf("<tr>\n");
            row_number ++;
            column_number = 1;//reset chi so cot ve mac dinh
        };
value:  T_CONSTANT{$$ = $1; print_td($1);column_number++;} |  //cập nhật giá trị
        '-' T_CONSTANT  %prec UMINUS{$$ = $2;print_td(-$2);column_number++;};//chấp nhận giá trị số âm
%%

int main() {
    printf("<table boder='1'>\n");
    printf("<tr>\n");
    yyparse();
    printf("\n</tr>\n");
    printf("</table>\n");
    return 0;
}
