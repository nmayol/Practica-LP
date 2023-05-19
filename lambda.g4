grammar lambda;
root : terme             // etiqueta es un terme
     ;
terme : '(' terme ')'                   # parentesi
     | terme terme                      # aplicacio
     | ('λ' | '\\') cap '.' terme       # abstraccio
     | LLETRA                           # lletra
     ;

cap: LLETRA+;
LLETRA : ('a'..'z');
WS  : [ \t\n\r]+ -> skip ;
