/*
3) Faça um programa que calcule e imprima o salário a ser transferido para um funcionário.
Para realizar o calculo receba o valor bruto do salário e o adicional dos benefícios.
O salário a ser transferido é calculado da seguinte maneira:

valor bruto do salário - percentual de imposto mediante a faixa salarial + adicional dos benefícios

Para calcular o percentual de imposto segue as aliquotas:

De R$ 0,00 a R$ 1100,00 = 5%
De R$ 1100,01 a R$ 2500,00 = 10%
Acima de R$ 2500,00 = 15%

Exemplo:
Entrada:
2000
250

Saída:
2050.00
*/
const {gets, print} = require('./funcoes-auxiliares3');

const valorSalarioBruto = gets();
const adicionalDosBeneficios = gets()

function percentual(valor){
    if(valor <= 1100){
        return 0.05;
    }else if(valor <= 2500){
        return 0.1;
    }else{
        return 0.15;
    }
}

const percentualDeImposto = percentual(valorSalarioBruto);
const valorAserTransferido = valorSalarioBruto - (valorSalarioBruto * percentualDeImposto) + adicionalDosBeneficios;

print(valorAserTransferido.toFixed(2));