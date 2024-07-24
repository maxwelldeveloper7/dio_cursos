// uma const lista de 1 a 10
const lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const cb = (value, i, listRef) => {
    console.log(value, i, listRef);
};

lista.forEach(cb);
// uso simples
lista.forEach((value) => console.log(value));

// um for
for (let i = 0; i < lista.length; i++) {
    const element = lista[i];
    cb(element, i, lista)
}