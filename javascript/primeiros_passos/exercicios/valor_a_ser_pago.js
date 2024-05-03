let valorDoProduto = 100;
//condições de pagamento
/*
Código condição de pagamento:
1 - À vista Débito, recebe 10% de desconto;
2 - À vista no Dinheiro ou PIX, recebe 15% de desconto;
3 - Em duas vezes, preço normal de etiqueta sem juros;
4 - Acima de duas vezes, preço normal de etiqueta mais juros de 10%
 */

let formaDePagamento = 3;

if (formaDePagamento === 1){
    valorDoProduto = valorDoProduto * 0.9;
} else if (formaDePagamento === 2){
    valorDoProduto = valorDoProduto * 0.85;
} else if (formaDePagamento === 4){
    valorDoProduto = valorDoProduto * 1.1;
}

console.log(`O valor a ser pago pelo produto é R$ ${valorDoProduto.toFixed(2)}`)
