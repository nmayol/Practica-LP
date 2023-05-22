grammar lc;


root : terme                                                 
     ;
terme : '(' terme ')'                   # parentesi
     | (MACRO '≡' terme)                # macro
     | (MACROINFIXA '≡' terme)          # macroI
     | MACRO                            # macroFormula
     | terme MACROINFIXA terme          # macroIFormula 
     | terme terme                      # aplicacio
     | ('λ' | '\\') cap '.' terme       # abstraccio
     | LLETRA                           # lletra 
     ;

cap: LLETRA+;
LLETRA : ('a'..'z');
MACRO : [A-Z][A-Z0-9]*;
MACROINFIXA: ~[a-zA-Z];
WS  : [ \t\n\r]+ -> skip;


