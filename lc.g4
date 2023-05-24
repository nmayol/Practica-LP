grammar lc;
root : terme                                                 
     ;
terme : '(' terme ')'                   # parentesi
     | terme terme                      # aplicacio
     | ('λ' | '\\') cap '.' terme       # abstraccio
     | LLETRA                           # lletra 
     | MACRO '≡' terme                  # macro
     | MACROINFIXA '≡' terme            # macroI
     | MACRO                            # macroFormula
     | terme MACROINFIXA terme          # macroIFormula 
     ;

cap: LLETRA+;
LLETRA: [a-z];
MACRO: [A-Z][A-Z0-9]*;
MACROINFIXA: ~[a-zA-Z \t\r\n];
WS: [ \t\r\n]+ -> skip;
