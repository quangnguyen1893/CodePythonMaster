%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Symbol {
    char* name;
    int value;
};

struct SymbolTable {
    struct Symbol** symbols;
    int numSymbols;
};

struct SymbolTable* symbolTable;

int yylex();
int yyerror(char* msg) {
    fprintf(stderr, "Error: %s\n", msg);
    return 0;
}

void initializeSymbolTable() {
    symbolTable = (struct SymbolTable*)malloc(sizeof(struct SymbolTable));
    symbolTable->symbols = NULL;
    symbolTable->numSymbols = 0;
}

struct Symbol* findSymbol(char* name) {
    for (int i = 0; i < symbolTable->numSymbols; i++) {
        if (strcmp(symbolTable->symbols[i]->name, name) == 0) {
            return symbolTable->symbols[i];
        }
    }
    return NULL;
}

void insertSymbol(char* name, int value) {
    struct Symbol* symbol = (struct Symbol*)malloc(sizeof(struct Symbol));
    symbol->name = strdup(name);
    symbol->value = value;

    symbolTable->numSymbols++;
    symbolTable->symbols = (struct Symbol**)realloc(symbolTable->symbols, symbolTable->numSymbols * sizeof(struct Symbol*));
    symbolTable->symbols[symbolTable->numSymbols - 1] = symbol;
}

void freeSymbolTable() {
    for (int i = 0; i < symbolTable->numSymbols; i++) {
        free(symbolTable->symbols[i]->name);
        free(symbolTable->symbols[i]);
    }
    free(symbolTable->symbols);
    free(symbolTable);
}

void printSymbolTable() {
    printf("Symbol Table:\n");
    for (int i = 0; i < symbolTable->numSymbols; i++) {
        printf("%s = %d\n", symbolTable->symbols[i]->name, symbolTable->symbols[i]->value);
    }
}

void executePrint(int value) {
    printf("PRINT: %d\n", value);
}

void executeBinaryOperation(char* operator) {
    printf("%s\n", operator);
}

void executeUnaryOperation(char* operator) {
    printf("%s\n", operator);
}

void executePush(int value) {
    printf("PUSH %d\n", value);
}

void executeAssignment(char* variable, int value) {
    insertSymbol(variable, value);
}

int evaluateVariable(char* variable) {
    struct Symbol* symbol = findSymbol(variable);
    if (symbol == NULL) {
        fprintf(stderr, "Error: Variable %s has not been declared\n", variable);
        exit(1);
    }
    return symbol->value;
}

%}

%union {
    char* identifier;
    int constant;
}

%token <identifier> T_IDENTIFIER
%token <constant> T_CONSTANT
%token T_PRINT
%left '+' '-'
%left '*' '/'
%nonassoc UMINUS

%%

Program    : Block ;

Block      : '{' DeclarationList StatementList '}' ;

DeclarationList : Declaration |
                  Declaration ';' DeclarationList ;

Declaration: T_IDENTIFIER { $$ = $1; } ;

StatementList: Statement |
               Statement ';' StatementList ;

Statement  : T_PRINT '(' Expression ')' { executePrint($3); } |
             T_IDENTIFIER '=' Expression { executeAssignment($1, $3); } ;

Expression : Expression '+' Expression { executeBinaryOperation("ADD"); } |
             Expression '-' Expression { executeBinaryOperation("SUB"); } |
             Expression '*' Expression { executeBinaryOperation("MUL"); } |
             Expression '/' Expression { executeBinaryOperation("DIV"); } |
             '-' Expression %prec UMINUS { executeUnaryOperation("UMINUS"); } |
             '(' Expression ')' |
             T_CONSTANT { executePush($1); } |
             T_IDENTIFIER { $$ = evaluateVariable($1); } ;

%%
int main() {
    initializeSymbolTable();
    yyparse();
    printSymbolTable();
    freeSymbolTable();
    return 0;
}
