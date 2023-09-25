class Bank:
    def __init__(self) -> None:
        self.details = {}

    def create_account(self,acc_number,balance):
        if acc_number in self.details:
            print("Account number already exist in our system")
        else:
            self.details[acc_number]=balance
    

    def deposit(self,acc_number,amount):
        if acc_number in self.details:
            self.details[acc_number]+=amount
        else:
            print("Wrong Account number")
    

    def withdrawl(self,acc_number,amount):
        if acc_number in self.details:
            if self.details[acc_number]>=amount:
                self.details[acc_number]-=amount
            else:
                print("Insufficiant anount")
        else:
            print("Wrong Account Number")
        
# Example usage
bank = Bank()
bank.create_account("acno1", 10000)