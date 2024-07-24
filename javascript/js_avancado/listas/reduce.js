// uma lista const de 1 a 10
const lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// reduzir a lista a um unico valor somado todos os numeros
const soma = lista.reduce((previous, current) => previous + current, 0);

console.log(soma);