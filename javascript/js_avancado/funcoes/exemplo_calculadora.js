
function adicao(x, y){
    return x + y;
}

function subtracao(x, y){
    return x - y;
}

function multiplicacao(x, y){
    return x * y;
}

function divisao(x, y){
    return x / y;
}

function calculadora(x, operacao, y){
    console.log(operacao(x, y));
}

calculadora(2, adicao, 3);