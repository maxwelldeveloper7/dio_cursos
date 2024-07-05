function imprimirTaboada(numero) {
    for (let i = 1; i <= 10; i++) {
        console.log(`${numero} x ${i} = ${numero * i}`);
    }
}

function criarTaboadas(){
    for (let i = 1; i <= 10; i++) {
        console.log(`\nTaboada de ${i}`) //chamar a funcao ${i}
        imprimirTaboada(i);
    }
}

criarTaboadas();