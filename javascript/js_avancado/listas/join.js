// uma const lista de 1 a 10
const lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// juntar esta lista com ;
const separador = lista.join(';');

console.log(separador);

// uma lista com 10 objetos pessoa
const pessoas = [
    { nome: 'João', idade: 25 },
    { nome: 'Maria', idade: 30 },
    { nome: 'José', idade: 35 },
    { nome: 'Ana', idade: 40 },
    { nome: 'Pedro', idade: 45 },
    { nome: 'Mariana', idade: 50 },
    { nome: 'Lucas', idade: 55 },
    { nome: 'Carla', idade: 60 },
    { nome: 'Rafael', idade: 65 },
    { nome: 'Julia', idade: 70 }
];

const pessoasFiltro = pessoas.filter((pessoa) => pessoa.nome.startsWith('A'))
console.log(pessoasFiltro)

// juntar esta lista e nomes de pessoas separados por ;
const nomes = pessoas.map(pessoa => pessoa.nome).join('; ');
console.log(nomes);

// agora uma combinação
const listaFiltrada = pessoas.map(pessoa => pessoa.nome).filter(nome => nome.startsWith('A')).join('; ');
console.log(listaFiltrada);
