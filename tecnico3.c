/*
Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?

O valor de soma é 78, pois mesmo que o valor atual de K seja 12, o loop irá parar, mas ainda é executado mais um vez, o que resulta em SOMA valendo 78. Segue codigo em C com o exemplo.
*/

#include <stdio.h>

int main () {
	int INDICE = 12, SOMA = 0, K = 1;
	
	while (K < INDICE) {
    	K = K + 1;
    	SOMA = SOMA + K;
	    printf("%d\n", SOMA);
	}
	printf("%d", SOMA);
}