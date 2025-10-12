function calculateRanking(victories, defeats) {
    let balance = victories - defeats
    let ranking = ""

    if (victories < 10) {
        ranking = "Ferro"
    } else if (victories >= 11 && victories <= 20) {
        ranking = "Bronze"
    } else if (victories >= 21 && victories <= 50) {
        ranking = "Prata"
    } else if (victories >= 51 && victories <= 80) {
        ranking = "Ouro"
    } else if (victories >= 81 && victories <= 90) {
        ranking = "Diamante"
    } else if (victories >= 91 && victories <= 100) {
        ranking = "Lendário"
    } else if (victories >= 101) {
        ranking = "Imortal"
    }

    return `O Herói tem de saldo de **${balance}** está no nível de **${ranking}**`
}

console.log(calculateRanking(100, 5))