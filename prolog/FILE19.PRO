%Si eres hombre entonces eres débil
%Hx->Dx
%Juan es hombre
%Hj
%.: Juan es débil

adolescente(luis). mujer(fer). temeroso(juan). hombre(juan).
debil(lalo). cobarde(miguel). debil(manuel). hombre(miguel).
hombre(jose). adolescente(manuel). mujer(minerva).
adolescente(minerva).
cobarde(X):-debil(X),temeroso(X).
debil(X):-hombre(X).
temeroso(X):-adolescente(X),mujer(X).


