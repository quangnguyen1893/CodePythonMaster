%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
	
	typedef struct {
		char name[32]; //giới hạn tên biến tối đa 32 ký tự.
		int val;
	} Variable;

	Variable VariableList[1000]; //Giới hạn tối đa 1000 biến.
	int n = 0;
	int err = 0;
	//Kiểm tra biến đã có trong danh sách chưa, nếu chưa trả về -1.
	int findVariable(const char *name) {
		for (int i = 0; i < n; i++)
			if (strcmp(name, VariableList[i].name) == 0)
			return i;
		return -1;
	}
	
	//Thêm biến tên name vào danh sách VariableList
	void addVariable(const char *name) {
		strcpy(VariableList[n].name, name);
		n = n + 1;
	}
	
	//Lấy giá trị của biến tên name
	int getValue(const char *name) {
		for (int i=0; i<n; i++){
			if (strcmp(name, VariableList[i].name) == 0) {
				return VariableList[i].val;
			}
		}
		return -1;
	}

	//Gán val vào biến tên name
	int setValue(const char *name, int val) {
		int index = findVariable(name);
		if (index != -1) {
			VariableList[index].val = val;
		}
		return -1;
	}

	// Hàm kiểm tra lỗi
	// int yylex();
	// void yyerror(const char *s);
	int yylex (void);
	int yyerror(const char *msg) {
		fprintf(stderr, "Error:%s\n", msg);
		return 0;
	}
%}

%union {
	int intValue;
	char strValue[32];
	// int errValue;
}

%token <intValue> T_CONSTANT
%token <strValue> T_ID
%type <intValue> Expression
%type <intValue> Bexpression
%token T_PRINT T_WHILE T_DO T_ENDO T_IF T_THEN
%token T_LE T_SE T_ET T_NET T_ELSE T_ENDIF
%token T_INT
%left '+' '-'
%left '*' '/'
%nonassoc UMINUS

%%
Program : Block ;
Block : '{' Slist '}' |
	 '{' Vardef Slist '}' ;
Vardef : T_INT Varlist ';' ;
Varlist : T_ID ',' 
Varlist
	{
		if (findVariable($1) == -1){
			addVariable($1);
			printf("DEFINE %s \n", $1);
		}
	}|
	T_ID {
		if (findVariable($1) == -1){
			addVariable($1);
			printf("DEFINE %s \n", $1);
		}
	} ;
Bexpression : Expression T_LE Expression {
		$$ = ($1 >= $3) ? 1 : 0;
		printf("COMPARE %d >= %d \n", $1, $3);
		}|
		Expression T_SE Expression {
		$$ = ($1 <= $3) ? 1 : 0;
		printf("COMPARE %d <= %d \n", $1, $3);
		}|
		Expression T_ET Expression {
		$$ = ($1 == $3) ? 1 : 0;
		printf("COMPARE %d == %d \n", $1, $3);
		}|
		Expression T_NET Expression {
		$$ = ($1 != $3) ? 1 : 0;
		printf("COMPARE %d != %d \n", $1, $3);
		}|
		Expression '<' Expression {
		$$ = ($1 < $3) ? 1 : 0;
		printf("COMPARE %d < %d \n", $1, $3);
		}|
		Expression '>' Expression{
		$$ = ($1 > $3) ? 1 : 0;
		printf("COMPARE %d > %d \n", $1, $3);
		} ;
Whilestatement : T_WHILE Bexpression T_DO
		Slist
		T_ENDO
	{
		printf("WHILESTAMENT: ");
		if ($2 == 1) {
			printf("True \n");
		}else {
			printf("False \n");
		}
	} ;
IfStament : T_IF Bexpression T_THEN Slist T_ELSE Slist T_ENDIF
		{printf("IFSTAMENT: ");
			if ($2 == 1) {
				printf("True \n");
			}else {
				printf("False \n");
			}
		}|
		T_IF Bexpression T_THEN Slist T_ENDIF
		{printf("If stament");
		if ($2 == 1) {
			printf("True \n");
		}else {
			printf("False \n");
		  }
		} ;
Slist : Stament |
	 Stament ';' Slist ;
Stament : T_PRINT '(' Expression ')' {
						if (err == 0){
						printf("%d\n", $3);
					       }
				         }|
		     T_ID '=' Expression {
		     setValue($1, $3);
		}|
		Whilestatement Stament|
		IfStament Stament| ;
		
Expression : Expression '+' Expression {printf("ADD\n"); $$ = $1 + $3;} |
	      Expression '-' Expression {printf("SUB\n"); $$ = $1 - $3;} |
	      Expression '*' Expression {printf("MUL\n"); $$ = $1 * $3;} |
	      Expression '/' Expression {printf("DIV\n"); $$ = $1 / $3;} |
		'-' Expression %prec UMINUS {printf("UMINUS\n"); $$ = - $2;} |
		'(' Expression ')' {$$ = $2;} |
		T_CONSTANT {printf("PUSH %d\n", $1); $$ = $1;}|
		T_ID { printf("POP %s\n", $1);
			int val = getValue($1);
			if (val == -1)
			{
				yyerror(strcat($1, " is not defined."));
				err = 1;
			}
			else
			{
				$$ = getValue($1);
			}
		} ;
		// T_ID {$$=getValue($1);printf("VARIABLE %s\n", $1);};
%%

int main() {
	yyparse();
	return 0;
}