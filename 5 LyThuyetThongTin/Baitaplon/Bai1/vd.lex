%{
#include "vd.tab.h"
%}

%%

"{"                return '{';
"}"                return '}';
"+"                return '+';
"-"                return '-';
"*"                return '*';
"/"                return '/';
"("                return '(';
")"                return ')';
";"                return ';';

[ \t\n\r]           {} //Bỏ qua các khoảng trắng

"print"             return T_PRINT;

[0-9]+              {
                    yylval = atoi(yytext); //Lưu giá trị của hằng
                    return T_CONSTANT;  //Trả về token T_CONSTANT
                    }                     
%%