/*
2) Faça um programa que receba N (quantidade de números) e seus respectivos valores.
Imprima o maior número par e o menor número impar.

    Exemplo:
        Entrada:
            5
            3
            4
            1
            10
            8

        Saida:
            Maior número par: 10
            Menor número impar: 1
*/

const {gets, print} = require('./funcoes-auxiliares2');

const n = gets();
let maiorNumeroPar = 0;
let menorNumeroImpar = Infinity;

for (let i = 0; i < n; i++) {
    const numero = gets();
    if (numero % 2 === 0) {
        if (numero > maiorNumeroPar) {
            maiorNumeroPar = numero;
        }
    } else {
        if (numero < menorNumeroImpar) {
            menorNumeroImpar = numero;
        }
    }
}

print('Quantidade de números: ' + n);

print('Maior número par: ' + maiorNumeroPar);
print('Menor número impar: ' + menorNumeroImpar);

