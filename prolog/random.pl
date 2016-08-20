:- initialization main.

loop(0).
loop(N,Stream) :-
	N > 0,
	forall( random(R), write(Stream, R)),
	write(Stream, '\n'),
	write(N),nl,
	M is N-1,
	loop(M,Stream);
	N is 0,
	loop(N).
	
main :-
	open("prolog.txt",write,Stream),
	loop(1000000,Stream),
	close(Stream),
	halt(0).
