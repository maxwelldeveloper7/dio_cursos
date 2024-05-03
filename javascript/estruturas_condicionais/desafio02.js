
console.log('Calculo com gasto de viagem');
let precoEtanol = 4.0
let precoGasolina = 5.6;
let tipoCombustivel = 'etanol'

if (tipoCombustivel === 'etanol'){
    precoCombustivel = precoEtanol;
}else if(tipoCombustivel === 'gasolina'){
    precoCombustivel = precoGasolina;
}

console.log('Preço do combustível: ', precoCombustivel);
let kmPorLitro = 10;
console.log('Gasto médio de combustível do carro por KM', kmPorLitro);
let distancia = 1;
console.log('Distância em Km da viagem: ', distancia);
let custoDaViagem = (distancia / kmPorLitro) * precoCombustivel;


console.log('O custo da viagem é de: R$', custoDaViagem.toFixed(2));