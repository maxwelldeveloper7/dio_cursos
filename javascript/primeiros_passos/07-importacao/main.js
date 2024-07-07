const { gets, print } = require('./funcoes-auxiliares');

const quantidadeDeAlunos = gets();
let maiorValor = 0;

for (let i = 0; i < quantidadeDeAlunos; i++) {
    const numerosSorteado = gets();    
    if (numerosSorteado > maiorValor) {
        maiorValor = numerosSorteado;
    }
}

print(maiorValor);

/*

    Uma salda contem 5 alunos e para cada aluno foi sorteado um número de 1 - 100.
    Faça um programa que receba os 5 números sorteados para os alunos e mostre o maior número sorteado.

    Dados de entrada:
    5
    50
    10
    98
    23

    Saída:
    98

*/
//const funcoes = require('./funcoes-auxiliares');
// funcoes.print('oi');
// console.log(funcoes.gets());

// // Object Destructuring
// const {gets, print} = require('./funcoes-auxiliares');

// print('oi');
// console.log(gets());