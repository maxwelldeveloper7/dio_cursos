const funcoes = require('./funcoes-auxiliares');

funcoes.print('oi');
console.log(funcoes.gets());

// Object Destructuring
const {gets, print} = require('./funcoes-auxiliares');

print('oi');
console.log(gets());