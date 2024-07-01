const notas = []
notas.push(5);
notas.push(10);
notas.push(7);
notas.push(8);
notas.push(4);
notas.push(6);
notas.push(3);
notas.push(1);
notas.push(9);

let soma = 0;

for (let i = 0; i < notas.length; i++) {
    const nota = notas[i];
    soma = soma + nota;
}

console.log(`A soma das notas é: ${soma}`)
console.log(`E media das notas é: ${soma/notas.length}`)