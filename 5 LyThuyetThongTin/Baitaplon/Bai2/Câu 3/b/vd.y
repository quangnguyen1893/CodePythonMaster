%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define atoa(x)
int row = 1;
int col = 1;
char htmlString[1000] = "";
const char *table = "<table border=\"1\">";
const char *tableEnd = "</table>";
const char *tr = "<tr>";
const char *trEnd = "</tr>";
const char *td = "<td>";
const char *tdEnd = "</td>";

void addValue(int val){
	char str[10];
	sprintf(str, "%d", val);
	if (row == 1 && col == 1){
		strcat(htmlString,table);
		printf("\n%s\n",table);
		strcat(htmlString,tr);
		printf("\t%s\n",tr);
	}
	if (col == 1) {
		printf("\t\t");
	}
	strcat(htmlString,td);
	printf("%s",td);
	strcat(htmlString,str);
	printf("%s",str);
	strcat(htmlString,tdEnd);
	printf("%s",tdEnd);
	col++;
}
void endLine(){
	strcat(htmlString,trEnd);
	printf("\n\t%s\n",trEnd);
	row++;
	col = 1;
}

void endTable(){
	strcat(htmlString,tableEnd);
	printf("%s\n",tableEnd);
}
void createHtmlFile(){
	FILE * file;
	file = fopen("./text.html", "w");
	if(file == NULL){
		printf("Unable to create file.\n");
		exit(EXIT_FAILURE);
	}
	fputs(htmlString, file);
	fclose(file);
	printf("text.html is OK\n");
}
// Hàm kiểm tra lỗi
int yylex();
	void yyerror(const char *s);

%}

%token T_CONSTANT T_UMINUS T_ENDL

%%
Rows : Row Rows | { printf("\n"); endTable();
createHtmlFile();} ;
Row : int | endl ;
int : T_CONSTANT { $$ = $1; addValue($1);
				 } |
	T_UMINUS T_CONSTANT { $$ = -$2; } ;
endl : T_ENDL { endLine() } ;
%%
int main() {
	yyparse();
	return 0;
}