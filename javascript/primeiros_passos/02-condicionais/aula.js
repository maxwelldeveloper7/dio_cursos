const numero = 10

const eNumeroPar = numero % 2 === 0;

if(numero === 0){
    console.log('O número é inválido');
}else if (eNumeroPar){
    console.log(`O numero ${numero} é par`);
}else{
    console.log(`O numero ${numero} é impar`);
}