grammar lambda;
root : terme             // etiqueta es un terme
     ;
terme : '(' terme ')'                   # parentesi
     | ('λ' | '\\') cap '.' terme       # abstraccio
     | terme terme                      # aplicacio
     | LLETRA                           # lletra
     ;

cap: LLETRA+;
LLETRA : ('a'..'z');
WS  : [ \t\n\r]+ -> skip ;
