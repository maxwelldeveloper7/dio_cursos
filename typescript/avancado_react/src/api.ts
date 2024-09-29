const conta = {
    email: 'maxwell@maxwell',
    password: '123456',
    name: 'Maxwell Chaves'
}

export const api = new Promise((resolve) => {
    setTimeout(() => {
        resolve(conta)
    }, 3000)
})