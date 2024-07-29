export abstract class DioAccount{
    private name: string;
    private accountNumber: number;
    private balance: number;

    constructor(name: string, accountNumber: number){
        this.name = name;
        this.accountNumber = accountNumber;
        this.balance = 0;
    }

    public deposit(amount: number): void{
        this.balance += amount;
    }

    public withdraw(amount: number): void{
        if(this.balance >= amount){
            this.balance -= amount;
        }else{
            console.log("Insufficient funds");
        }
    }

    public getBalance(): number{
        return this.balance;
    }
}