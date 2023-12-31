// Define a grammar called Grammar
grammar Grammar;

CLASS: 'class' | 'CLASS';
INHERITS: 'inherits' | 'INHERITS';
STRING: '"' .*? '"';
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

ID : [a-z]([a-zA-Z0-9]|'_')*;
TYPE : [A-Z]([a-zA-Z0-9]|'_')*;
WS: [ \n\t\r] -> skip;
LINE_COMMENT : '--' (~ '\n')* '\n'? -> skip;
INIT_COMMENT: '(*';
FINISH_COMMENT: '*)';
COMMENT: INIT_COMMENT (COMMENT | .)*? FINISH_COMMENT -> skip;
r  : program ;

program: (classDef SEMICOLON)+ ;
classDef: CLASS TYPE (INHERITS TYPE)? LBRACKET (feature SEMICOLON)* RBRACKET                    #CLASS_DEFINITION;               
feature: 
        ID LPAREN (formal (COMMA formal)* )? RPAREN COLON TYPE LBRACKET expr RBRACKET           #DEFINITION_METHOD_PARAMS
        | ID COLON TYPE (ASSIGN expr)?                                                          #DEFINITION_PARAMS ;
formal: ID COLON TYPE;
formalAssign: ID COLON TYPE ( ASSIGN expr )?;

expr:
        expr (AT TYPE)? DOT ID LPAREN ( expr (COMMA expr)* )* RPAREN                            #DISPATCH
        | ID LPAREN ( expr (COMMA expr)* )? RPAREN                                              #CALL
        | IF expr THEN expr ELSE expr FI                                                        #IF_CLAUSE
        | WHILE expr LOOP expr POOL                                                             #WHILE_CLAUSE
        | LBRACKET (expr SEMICOLON)+ RBRACKET                                                   #BLOCK
        | LET formalAssign (COMMA formalAssign)* IN expr                                        #LET_PASS
        | NEW TYPE                                                                              #NEWOBJ
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
        | FALSE                                                                                 #FALSE
        | <assoc=right>    ID ASSIGN expr                                                       #ASSIGN_VAL;
