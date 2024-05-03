const peso = 87
const altura = 1.87

const imc = peso / Math.pow(altura, 2);

let conclusao = 'NaN';

if (imc < 18.5){
    conclusao = 'abaixo do peso'
} else if (imc >= 18.5 && imc <= 25){
    conclusao = 'com peso normal'
} else if (imc >= 25 && imc <=30){
    conclusao = 'acima do peso'
} else if (imc >=30 && imc<= 40){
    conclusao = 'obeso'
} else if (imc > 40){
    conclusao = 'com obesidade grave'
}

console.log(`O seu IMC é ${imc.toFixed(2)} e você está ${conclusao}`);