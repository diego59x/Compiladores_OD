// Define a grammar called Hello
grammar Hello;
program: (class';')+ ;
class: CLASS TYPE (INHERITS TYPE)? '{' (feature';')* '}' ; 
feature: 
        ID '(' (formal (','formal)* )? ')' ':' TYPE '{' expr '}'
        | ID ':' TYPE ('<-' expr)? ;
formal: ID ':' TYPE;

expr: 
        ID '<-' expr
        | expr('@' TYPE)'.'ID( ( expr(','expr)* ))?
        | ID '(' ( expr (','expr)* )? ')'
        | IF expr THEN expr ELSE expr FI
        | WHILE expr LOOP expr POOL
        | '{' (expr';')+ '}'
        | LET ID ':' TYPE ( '<-' expr )? (',' ID ':' TYPE ('<-' expr)?)* IN expr
        | NEW TYPE
        | ISVOID expr
        | expr '+' expr
        | expr '-' expr
        | expr TIMES expr
        | expr DEVIDE expr
        | '~'expr
        | expr BIGGER expr
        | expr BIGGEREQUALS expr
        | expr EQUALS expr
        | NOT '('expr')'
        | '('expr')' 
        | ID
        | INTEGER
        | STRING
        | TRUE
        | WS
        | FALSE;

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
DEVIDE: '/';
TIMES: '*';
TRUE: 'true';
FALSE: 'false';

ID : [a-z][a-zA-Z0-9_]* ;
TYPE : [A-Z][a-zA-Z0-9_]* ;
WS : [ \t\r\n]+ -> skip ;

r  : program ;