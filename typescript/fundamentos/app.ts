import { PeopleAccount } from "./class/PeopleAccount";
import { CompanyAccount } from "./class/CompanyAccount";



const newAccount = new PeopleAccount(1,"John Doe", 123456);
console.log(newAccount);

const newCompanyAccount = new CompanyAccount(1, "ABC Company", 789012);
console.log(newCompanyAccount);
newCompanyAccount.getLoan(1000);
console.log(newCompanyAccount.getBalance());
