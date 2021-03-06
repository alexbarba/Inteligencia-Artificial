hijo(jesus,jose,maria).  % Jesús es hijo de José y María
hija(magdalena,jose,maria).  % Magdalena es hija de José y María
hijo(juan,jesus,martha).
hija(daniela,jesus,martha).
hijo(roberto,pedro,magdalena).
hija(patricia,pedro,magdalena).

% X es papá de Y
papá(X,Y):-hijo(Y,X,_).
papá(X,Y):-hija(Y,X,_).

% X es mamá de Y
mamá(X,Y):-hijo(Y,_,X).
mamá(X,Y):-hija(Y,_,X).

% X es hermano de Y

hermano(X,Y):-hijo(X,P,M),hijo(Y,P,M),X\=Y.
hermano(X,Y):-hijo(X,P,M),hija(Y,P,M).

% X es hermana de Y

hermana(X,Y):-hija(X,P,M),hijo(Y,P,M).
hermana(X,Y):-hija(X,P,M),hija(Y,P,M),X\=Y.

% X es abuelo de Y

abuelo(X,Y):-papá(X,Z),papá(Z,Y).
abuelo(X,Y):-papá(X,Z),mamá(Z,Y).

%X es abuela de Y

%X es prima de Y

prima(X,Y):-hija(X,P,M),hijo(Y,Q,N),hermano(P,Q).
prima(X,Y):-hija(X,P,M),hija(Y,Q,N),hermano(P,Q).
prima(X,Y):-hija(X,P,M),hijo(Y,Q,N),hermano(P,N).
prima(X,Y):-hija(X,P,M),hija(Y,Q,N),hermano(P,N).
prima(X,Y):-hija(X,P,M),hijo(Y,Q,N),hermana(M,Q).
prima(X,Y):-hija(X,P,M),hija(Y,Q,N),hermana(M,Q).
prima(X,Y):-hija(X,P,M),hijo(Y,Q,N),hermana(M,N).
prima(X,Y):-hija(X,P,M),hija(Y,Q,N),hermana(M,N).

% X es prima de Y 

prima(X,Y):-hija(X,_,_),abuelo(Z,X),abuelo(Z,Y),not hermana(X,Y),X\=Y.

% papá,mamá,herman@,abuel@,niet@,prim@,ti@,sobrin@.