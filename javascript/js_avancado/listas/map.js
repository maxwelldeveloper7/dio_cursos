
class Pessoa {
    constructor(nome, idade) {
        this.nome = nome;
    }
}

// uma lista const com 10 pessoas
const pessoas = [
    new Pessoa('João', 20),
    new Pessoa('Maria', 25),
    new Pessoa('Pedro', 30),
    new Pessoa('Ana', 35),
    new Pessoa('Carlos', 40),
    new Pessoa('Mariana', 45),
    new Pessoa('Lucas', 50),
    new Pessoa('Laura', 55),
    new Pessoa('Fernando', 60),
    new Pessoa('Beatriz', 65)
];

// converter esta lista de pessoas em uma lista <li>
const listaHtml = pessoas.map(pessoa => `<li>${pessoa.nome}</li>`);
console.log(listaHtml);

// converter esta lista de pessoas em uma lista de nomes
const nomes = pessoas.map(pessoa => pessoa.nome);
console.log(nomes);

