import { DioAccount } from "./DioAccount";

export class CompanyAccount extends DioAccount{
    private company_id: number;

    constructor(company_id: number, name: string, accountNumber: number){
        super(name, accountNumber);
        this.company_id = company_id;
    }

    getLoan(amount: number): void{
        console.log("You got a loan of " + amount);
        this.deposit(amount);
    }
}