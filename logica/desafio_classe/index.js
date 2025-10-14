class heroi{
    constructor(nome, idade, tipo){
        this.nome = nome
        this.idade = idade
        this.tipo = tipo
    }

    atacar(){
        let ataque = ""
        if (this.tipo === "mago"){
            ataque = "magia"
        } else if (this.tipo === "guerreiro"){
            ataque = "espada"
        } else if (this.tipo === "monge"){
            ataque = "artes marciais"
        } else if (this.tipo === "ninja"){
            ataque = "shuriken"
        }
        console.log(`O ${this.tipo} ${this.nome} atacou usando ${ataque}`)
    }

}

calebe = new heroi("Calebe", 9, "guerreiro")
calebe.atacar()
maxwell = new heroi("Maxwell", 46, "monge")
maxwell.atacar()
