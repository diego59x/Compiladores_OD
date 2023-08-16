// Define a grammar called Hello
grammar Hello;
program: (class SEMICOLON)+ ;
class: CLASS TYPE (INHERITS TYPE)? LBRACKET (feature SEMICOLON)* RBRACKET ; 
feature: 
        ID LPAREN (formal (COMMA formal)* )? RPAREN COLON TYPE LBRACKET expr RBRACKET           #DEFINITION_METHOD_PARAMS
        | ID COLON TYPE (ASSIGN expr)?                                                          #DEFINITION_PARAMS ;
formal: ID COLON TYPE;

expr: 
        (ID ASSIGN expr)+                                                                       #ASSIGN_VAL
        | expr(AT TYPE) DOT ID( ( expr(COMMA expr)* ))?                                         #EXPR_NOT_KNOWN1
        | ID LPAREN ( expr (COMMA expr)* )? RPAREN                                              #EXPR_NOT_KNOWN2
        | IF expr THEN expr ELSE expr FI                                                        #IF_CLAUSE
        | WHILE expr LOOP expr POOL                                                             #WHILE_CLAUSE
        | LBRACKET (expr SEMICOLON)+ RBRACKET                                                   #OBJ_DEF
        | LET ID COLON TYPE ( ASSIGN expr )? (COMMA ID COLON TYPE (ASSIGN expr)?)* IN expr      #DEFINITION_ASSIGN
        | (NEW TYPE)+                                                                           #DECLARE_TYPE
        | ISVOID expr                                                                           #VOID_EXPR
        | expr PLUS expr                                                                        #SUM
        | expr MINUS expr                                                                       #MINUS
        | expr TIMES expr                                                                       #TIMES
        | expr DIVIDE expr                                                                      #DIVIDE
        | TILDE expr                                                                            #TILDE
        | expr BIGGER expr                                                                      #BIGGER
        | expr BIGGEREQUALS expr                                                                #BIGGEREQUALS
        | expr EQUALS expr                                                                      #EQUALS
        | NOT LPAREN expr RPAREN                                                                #NOT
        | LPAREN expr RPAREN                                                                    #EXPR_PARAMS
        | ID                                                                                    #ID
        | INTEGER                                                                               #INTEGER
        | STRING                                                                                #STRING
        | TRUE                                                                                  #TRUE
        | FALSE                                                                                 #FALSE;

CLASS: 'class' | 'CLASS';
INHERITS: 'inherits' | 'INHERITS';
STRING: '"'.*'"';
INTEGER: [0-9]+;
IF: 'if' | 'IF';
FI: 'fi' | 'FI';
ELSE: 'else' | 'ELSE';
WHILE: 'while' | 'WHILE';
LOOP: 'loop' | 'LOOP';
POOL: 'pool' | 'POOL';
LET: 'let' | 'LET';
IN: 'in' | 'IN';
THEN: 'then' | 'THEN';
NEW: 'new' | 'NEW';
ISVOID: 'isvoid' | 'ISVOID';
NOT: 'not' | 'NOT';
EQUALS: '=';
BIGGER: '<';
BIGGEREQUALS: '<=';
DIVIDE: '/';
TIMES: '*';
TRUE: 'true';
FALSE: 'false';
LPAREN: '(';
RPAREN: ')';
LBRACKET: '{';
RBRACKET: '}';
SEMICOLON: ';';
PLUS: '+';
MINUS: '-';
ASSIGN: '<-';
TILDE: '~';
COLON: ':';
COMMA: ',';
DOT: '.';
AT: '@';

ID : [a-z][a-zA-Z0-9_]* ;
TYPE : [A-Z][a-zA-Z0-9_]* ;
WS: [ \n\t\r] -> skip;
r  : program ;