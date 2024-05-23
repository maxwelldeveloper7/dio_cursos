function escrevaMeuNome(nome){
    return 'Meu nome é:', nome;
}

function verificaMaiorIdade(idade, meuNome){
    let nome = escrevaMeuNome(meuNome)
    if(idade >= 18){
        console.log(nome,idade,'anos - Maior idade.')
    }else{
        console.log(nome,idade,'anos - Menor idadae.')
    }
}

function aplicarDesconto(valor, desconto){
    return valor - (valor * desconto / 100);
}

function aplicarJuro(valor, juro){
    return valor + (valor * juro / 100);
}

function valorASerPago(valorDoProduto, formaDePagamento){
    if (formaDePagamento === 1){
        valorDoProduto = aplicarDesconto(valorDoProduto, 10);
    } else if (formaDePagamento === 2){
        valorDoProduto = aplicarDesconto(valorDoProduto, 15);
    } else if (formaDePagamento === 4){
        valorDoProduto = aplicarJuro(valorDoProduto, 10);
    }

    console.log(`O valor a ser pago pelo produto é R$ ${valorDoProduto.toFixed(2)}`)
}

valorASerPago(100,4)