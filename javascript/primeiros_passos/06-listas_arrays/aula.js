const notas = [];

notas.push(5);
notas.push(7);
notas.push(8);
notas.push(2);
notas.push(5);



console.log(notas.length)

let soma = 0;

notas.forEach(element => {
    soma += element;
});

media = soma / notas.length;

console.log(`A média das notas é: ${media}`)