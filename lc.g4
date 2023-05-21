grammar lc;


root : terme                            
     ;
terme : '(' terme ')'                   # parentesi
     | terme terme                      # aplicacio
     | ('λ' | '\\') cap '.' terme       # abstraccio
     | LLETRA                           # lletra
     | MACRO '≡' terme                  # macro
     ;

cap: LLETRA+;
LLETRA : ('a'..'z');
MACRO : [A-Z][A-Z0-9]*;
WS  : [ \t\n\r]+ -> skip;


