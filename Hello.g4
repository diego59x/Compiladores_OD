// Define a grammar called Hello
grammar Hello;

expr: '('expr')' 
        | NOT '('expr')';

CLASS: 'class' | 'CLASS';
ELSE: 'else' | 'ELSE';
FALSE: 'false';
FI: 'fi' | 'FI';
IF: 'if' | 'IF';
IN: 'in' | 'IN';
INHERITS: 'inherits' | 'INHERITS';
ISVOID: 'isvoid' | 'ISVOID';
LOOP: 'loop' | 'LOOP';
POOL: 'pool' | 'POOL';
THEN: 'then' | 'THEN';
WHILE: 'while' | 'WHILE';
NEW: 'new' | 'NEW';
NOT: 'not' | 'NOT';
TRUE: 'true';


STRING: '"'.*'"';
INTEGER: [0-9]+;
ID : [a-zA-Z_][a-zA-Z0-9_]* ;

r  : INTEGER ;
WS : [ \t\r\n]+ -> skip ;