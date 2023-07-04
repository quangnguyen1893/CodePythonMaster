%{
#include "vd.tab.h"
%}
%%
[{}+\-*/();=,] return yytext[0];
">=" 			return T_LE;
"<="			return T_SE;
"=="			return T_ET;
"!="			return T_NET;
[<>=]			return yytext[0];
[ \t\n\r] 		{} //Bỏ qua các khoảng trắng
"print" 		return T_PRINT;
"int" 			return T_INT;
"while"			return T_WHILE;
"do" 			return T_DO;
"endo" 			return T_ENDO;
"if" 			return T_IF;
"then" 			return T_THEN;
"else" 			return T_ELSE;
"endif" 		return T_ENDIF;
[0-9]+ 		{
			yylval.intValue = atoi(yytext);
			//Lưu giá trị của hằng
			return T_CONSTANT;
			//Trả về token T_CONSTANT
}
[a-z][A-Za-z0-9]* {
			strcpy(yylval.strValue, yytext);
			//Copy tên biến
			return T_ID; //Trả về token T_ID
			}
%%