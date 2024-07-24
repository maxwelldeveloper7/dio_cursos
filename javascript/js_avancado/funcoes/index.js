// named function declaration
function nomeDaFuncao() {
    console.log('nomeDaFuncao');
}

// named function expression
const nomeDeOutraFuncao = function () {
    console.log('nomeDeOutraFuncao');
}

// named arrow function
const arrowFunction = () => {
    console.log('arrowFunction');
}

// IIFE (Immediately Invoked Function Expression)
(function() {
    console.log('IIFE');
})()

// closures
function closure() {
    const nome = 'Closure';

    function exibeNome() {
        console.log(nome);
    }

    exibeNome();
}
