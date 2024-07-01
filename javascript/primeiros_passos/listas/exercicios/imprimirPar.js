const numeros = [];

for (let i = 0; i < 100; i++) {
    numeros.push(i);
}

console.log('Mostrando números pares de 1 a 100')

for (let i = 0; i < 100; i++) {
    if(i % 2 == 0){
        console.log(`${i}`);
    }
}