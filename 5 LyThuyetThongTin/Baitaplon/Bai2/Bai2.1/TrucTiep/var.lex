%{
#include "var.tab.h"
%}
%%
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
"^"				return '^';
[ \t\n\r]		{}
"print"			return T_PRINT;
"int"			return T_INT;
[0-9]+			{
					yylval.intValue = atoi(yytext);
					return T_CONSTANT;
				}
[a-zA-Z_][a-zA-Z0-9_]*	{
					strcpy(yylval.strValue, yytext);
					return T_ID;
				}
%%