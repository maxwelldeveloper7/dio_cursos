// uma lista const de 1 a 10
const lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// filtrar numeros pares
const pares = lista.filter((numero) => {
    return numero % 2 === 0;
});

console.log(pares)