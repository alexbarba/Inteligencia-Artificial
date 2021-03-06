% está(elemento,lista)

está(E,[E|_]).
está(E,[_|L]):-está(E,L).

%cuenta(lista,cantidad)

cuenta([],0).
cuenta([_|L],S):-cuenta(L,R),S is R+1.

% encontrar(lista,posicion,elemento)

encontrar([E|_],1,E).
encontrar([_|L],P,E):-Q is P-1,encontrar(L,Q,E).

% mayor(lista,max)

mayor([E],E).
mayor([E|L],M):-mayor(L,M),E=<M.
mayor([E|L],E):-mayor(L,M),E>M.

% unir(lista1,lista2,listares)

unir([],L,L).
unir([E|L],L2,[E|R]):-unir(L,L2,R)

