const pessoa = {
    idade: 18
}

const maxwell = {
    nome: 'maxwell',
    idade: 45,
    __proto__: pessoa
}

console.log(maxwell.idade) // 45
