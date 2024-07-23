function Pessoa(nome, idade) {
    this.nome = nome
    this.idade = idade
}

Pessoa.prototype.falar = function() {
    console.log(`Meu nome é ${this.nome}`)
}

const maxwell = new Pessoa('Maxwell', 45);
maxwell.falar(); // Meu nome é Maxwell

const pessoa = {
    genero: 'Masculino'
}

Pessoa.call(pessoa, 'nome', 30)

console.log(pessoa) // { genero: 'Masculino', nome: 'nome', idade: 30 }

Pessoa.apply(pessoa, ['nome', 30])