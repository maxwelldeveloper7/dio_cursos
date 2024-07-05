let nota1 = 7;
let nota2 = 7;
let nota3 = 10;

let media = (nota1 + nota2 + nota3) / 3;

resultado = 'NaN';

if (media < 5){
    resultado = 'foi reprovado';
}else if (media >= 5 && media <=7){
    resultado = 'está em recuperação';
}else{
    resultado = 'Passou de semestre';
}

console.log(`O aluno ${resultado}, sua nota média foi ${media.toFixed(2)}`)