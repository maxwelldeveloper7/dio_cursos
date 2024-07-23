
var var1 = 10;
var var2 = 'teste';

console.log(var1 + var2); // 10teste

var var3 = '20';

console.log(var1 + var3); // 1020

console.log(var1 - var3); // -10

console.log(var1 * var3); // 200

console.log(var1 / var2); // NaN

if(true){
    var var4 = 10;
}
console.log(var4); // 10

if(true){
    let var5 = 10;
}
console.log(var5); // ReferenceError: var5 is not defined

if(true){
    const var6 = 10;
}
console.log(var6); // ReferenceError: var6 is not defined

const var7 = 10;