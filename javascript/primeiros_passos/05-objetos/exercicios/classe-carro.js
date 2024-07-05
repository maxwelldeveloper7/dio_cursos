class Carro{
    marca;
    cor;
    gastoPorKm;

    constructor(marca, cor, gastoPorKm){
        this.marca = marca;
        this.cor = cor;
        this.gastoPorKm = gastoPorKm;
    }

    valorGastoParaPercurso(quilometragem, precoCombustivel){
        return ((quilometragem * this.gastoPorKm) * precoCombustivel).toFixed(2);
    }
}

const carro = new Carro('Ford', 'Preto', 1/12);
console.log(carro.valorGastoParaPercurso(100, 5));