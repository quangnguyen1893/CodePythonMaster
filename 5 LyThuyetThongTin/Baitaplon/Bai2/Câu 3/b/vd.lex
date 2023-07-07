%{
#include "vd.tab.h"
%}

%%
[ \t\r] 	{} //Bỏ qua các khoảng trắng
"-" 		return T_UMINUS;
"\n" 		return T_ENDL;

[0-9]+ 	{
			yylval = atoi(yytext); //Lưu giá trị của hằng
			return T_CONSTANT; //Trả về token T_CONSTANT
		}
%%