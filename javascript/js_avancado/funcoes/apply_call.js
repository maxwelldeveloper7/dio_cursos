const pessoa = {
    nome: 'maxwell',
    idade: 45
}

function gritar(prefixo){
    console.log(prefixo, this.nome)
}


gritar.apply(pessoa, ['Olaaaa'])
gritar.call(pessoa, 'Olaaaaa')
