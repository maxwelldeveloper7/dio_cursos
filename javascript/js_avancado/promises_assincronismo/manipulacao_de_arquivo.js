const fs = require('fs');

const path = require('path');

const filePath = path.resolve(__dirname, 'tarefas.csv');

const promessaDaLeituraDoAquivo = fs.promises.readFile(filePath);

promessaDaLeituraDoAquivo
    .then((arquivo) => arquivo.toString('utf-8'))
    .then((textoArquivo) => textoArquivo.split('\n').slice(1))
    .then((linhasSemCabecalho) => linhasSemCabecalho.map((linha) => {
        const [nome, feito] = linha.split(';');
        return{
            nome,
            feito: feito === 'true'
        }
    }))
    .then((listaDeTarefas) => console.log(listaDeTarefas))
    .catch((erro) => console.error(erro))