const pessoa = {
    genero : 'masculino'
}


const maxwell = {
    nome: 'maxwell',
    idade: 45,
    __proto__: pessoa   
}

console.log(maxwell.genero);

function Pessoa(nome, idade){
    this.nome = nome;
    this.idade = idade;
}

Pessoa.prototype.falar = function () {
    console.log(`Meu nome é: ${this.nome}`)
}


class Pesssoa{
    constructor(nome, idade){
        this.nome = nome;
        this.idade = idade;
    }

    falar () {
        console.log(`Meu nome é: ${this.nome}`);
    }
}
