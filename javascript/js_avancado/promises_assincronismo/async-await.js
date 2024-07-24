const fs = require('fs');

const path = require('path');

const filePath = path.resolve(__dirname, 'tarefas.csv');


async function buscarArquivo(){
    try{
        const arquivo = await fs.promises.readFile(filePath);
        const textoDoArquivo = arquivo.toString('utf-8');
        console.log(textoDoArquivo);        
    }catch(erro){
        console.error(erro);
    } finally{
        console.log('Final do programa');
    }
}

buscarArquivo();