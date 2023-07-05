%{
#include "vd.tab.h"
%}
%%
"int"			return T_INT;
"="				return '=';
","				return ',';
"{"				return '{';
"}"				return '}';
"+"				return '+';
"-"				return '-';
"*"				return '*';
"/"				return '/';
"("				return '(';
")"				return ')';
";"				return ';';
"<"				return T_LESSTHAN;
"<="			return T_LESSTHAN_EQUAL;
">"				return T_GREATER;
">="			return T_GREATER_EQUAL;
"=="			return T_EQUAL;
"!="			return T_NOT_EQUAL;
"while"			return T_WHILE;
"do"			return T_DO;
"endo"			return T_ENDO;
"if"			return T_IF;
"then"			return T_THEN;
"else"			return T_ELSE;
"endif"			return T_ENDIF;
[ \t\n\r]		{}
"print"			return T_PRINT;
[0-9]+			{
					yylval.intValue = atoi(yytext);
					return T_CONSTANT;
				}
[a-zA-Z_][a-zA-Z0-9_]*	{
					strcpy(yylval.strValue, yytext);
					return T_ID;
				}
%%