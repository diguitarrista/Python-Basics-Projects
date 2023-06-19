# The main example of how oriented object programming works taught in the courses is a simulated bank. 
# The goal here is to create different bank accounts that have the same characteristcs and operate with them.
# In this example I created two classes, Account and Operation. I generated five random bank accounts in the format
# that I proposed, so you can access one of them and operate or you can create a new bank account. 
# I'm not using this in an academic level or for commercial purposes. This code is only to demonstrate programming technics.
# This code was all written by me (@diguitarrista) and was inspired by a project from the courses at Alura Online Programming School. 

import random
import datetime

# This is a simple bank account dataset. It was generated randomly. 
accounts = {
    "name": ["Alice", "Bob", "Charlie", "Dave", "Eve"],
    "password": ["abc123", "def456", "ghi789", "jkl012", "mno345"],
    "number": [1234, 5678, 9012, 3456, 7890],
    "agency": [123456, 234567, 345678, 456789, 567890],
    "balance": [10000, 20000, 30000, 40000, 50000],
    "transactions": [{"Transfered": [], "Deposited": [], "Withdrawn": [], "Received": []},
    {"Transfered": [], "Deposited": [], "Withdrawn": [], "Received": []},
    {"Transfered": [], "Deposited": [], "Withdrawn": [], "Received": []},
    {"Transfered": [], "Deposited": [], "Withdrawn": [], "Received": []},
    {"Transfered": [], "Deposited": [], "Withdrawn": [], "Received": []}]
    }

# Creates the class Account. This class will have the person's account information.
class Account:
    def __init__(self, name, agency, number, password, balance, transactions):
        self.name = name
        self.agency = agency
        self.number = number
        self.password = password
        self.balance = balance
        self.transactions = transactions
    
    def account_status(self, name, agency, number, password, balance, transactions):
        return [self.name, self.password, self.number, self.agency, self.balance, self.transactions]

    def show_statement(self, agency, number, balance):
        print()
        print("--------------------------------------------------------------------")
        print("Account number:" , self.number, "Account agency:", self.agency)
        print("Balance: $", self.balance)
        print("--------------------------------------------------------------------")

    def show_informations(self, name, agency, number, password, balance):
        print()
        print("--------------------------------------------------------------------")
        print("Name:", self.name, "Password:", self.password)
        print("Account number:" , self.number, "Account agency:", self.agency)
        print("Balance: $", self.balance)
        print("--------------------------------------------------------------------")
        print()

# Creates the class Operation. This class will have all the bank operations.       
class Operation:
    def __init__(self):
        pass
    
    def create_account(self):
    # The user inputs the name and password, number and agency will be random numbers.
        name = str(input("Please inform your name: "))
        # Check if the user name is a digit or has any digits in the name.
        check_name = True
        while check_name:
            for letter in name:
                if letter.isdigit():
                    print()
                    print("You can't have numbers in your name yet.")
                    print()
                    name = str(input("Please inform your name: "))    
            if len(name) == 0 or name == " " or name.isdigit():
                print()
                print("> You have to put your name and not an empty space or numbers (yet). <")
                print()
                name = str(input("Please informe your name: "))
            else:
                check_name = False
        print()
        
        password = str(input("Type a password of 6 that can contain letters, numbers or special characters: "))
        # Check if the password has 6 characters.
        check_password = True
        while check_password:
            if len(password) < 6:
                print()
                print("> The password must have 6 characters. <")
                print()
                password = str(input("Type a password of 6 that can contain letters, numbers or special characters: "))
            else:
                check_password = False
                
        # Generate the account number and agency.
        number = random.randint(1000, 9999)
        agency = random.randint(100000, 999999)

        # Create the account.
        balance = 0
        transactions = {"Transfered": [], "Deposited": [], "Withdrawn": [], "Received": []}
        account = Account(name, agency, number, password, balance, transactions)
        person_account = account.account_status(name, agency, number, password, balance, transactions)
        print()
        print("Here is your account information:")
        print("Name:", person_account[0])
        print("Password:", person_account[1])
        print("Number:", person_account[2])
        print("Agency:", person_account[3])
        print("Balance:", person_account[4])
        print()

        return account

    def access_account(self, accounts):
        check_account = True
        while check_account:
            try:
                number = int(input("Type your account number: "))
                agency = int(input("Type your aggency number: "))
                password = input("Type your password: ")
                check_account = False
            except ValueError:
                print("> The number and the agency must be integers <")
                print()
                
        # Check the number, agency and password to access the account.
        if number in accounts["number"]:
            for n in accounts["number"]:
                if number == n:
                    number_index = accounts["number"].index(n)
                    if agency == accounts["agency"][number_index] and password == accounts["password"][number_index]:
                        print()
                        print("> You have accessed your account <") 
                        return accounts["number"][number_index]
                    else:
                        print()
                        print("> Wrong information! Try again <")
                        print()
                        return 0
        else:
            print()
            print("> Wrong information! Try again <")
            print()
            return 0
            
    def deposit(self):
        # Check if the user input is a number.
        check_money = True
        while check_money:
            try:
                deposit_value = float(input("How much money do you want to deposit in the PyBank: "))
                print()
                if deposit_value < 0:
                    print()
                    print("> You can't deposit negative values <")
                    print()
                else:
                    check_money = False
            except ValueError:
                print()
                print("> You must type a number in the format 10.0. <")
                print()

        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
        print("You have deposited $", deposit_value, "at", formatted_date)

        return [deposit_value, formatted_date]

    def withdraw(self, account):
        acc = account
        check_balance = True
        check_password = True

        # Check the account's balance.
        while check_balance:
            check_value = True
            while check_value:
                try:
                    withdraw_value = float(input("How much do you want to withdraw: "))
                    if withdraw_value < 0:
                        print()
                        print("> You can't withdraw negative values <")
                        print()
                    else:
                        check_value = False
                except ValueError:
                    print()
                    print("> You must type a number. <")
                    print()
                    
            if withdraw_value <= acc.balance:
                check_balance = False
                # Check the account's password.
                attempts = 3
                while check_password:
                    if attempts > 0:
                        print()
                        password = input("Please type your password to confirm the transaction: ")
                        if password != acc.password:
                            attempts -= 1
                            print()
                            print("> Wrong password ! Number the attempts left:", attempts, "<")
                            print()
                        else:
                            check_password = False
                            current_date = datetime.datetime.now()
                            formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
                            print()
                            print("You withdraw", str(withdraw_value), "at", formatted_date)
                            return [withdraw_value, formatted_date]
                    elif attempts == 0:
                        print()
                        print("> You have exceeded the number of attempts ! <")
                        print()
                        return [0, 0]     
            else:
                print()
                print("> You don't have enough money! <")
                print()
                value = 0
                check_balance = False
                return [0, 0]

    def transfer(self, bank_accounts, account):
        bank_accs = bank_accounts
        acc = account
        print("Inform the following information:")
        
        # Check the account info that the user is trying to transfer.
        check_info = True
        while check_info:
            try:
                name = input("The name of the account holder: ")
                number = int(input("The account number: "))
                agency = int(input("The account agency: "))
                check_info = False
            except ValueError:
                print()
                print("> The number and the agency must be integers. <")
                print()
        
        if name in bank_accs["name"]:
            name_index = bank_accs["name"].index(name)
            if number == bank_accs["number"][name_index] and agency == bank_accs["agency"][name_index]:
                check_transfer = True
                while check_transfer:
                    try:
                        transfer_value = float(input("How much do you want to transfer: "))
                        if transfer_value < 0:
                            print()
                            print("> You can't transfer negative values <")
                            print()
                        # Check the balance from the user's account.
                        elif transfer_value > acc.balance:
                            print()
                            print("> You don't have enough balance <")
                            print()
                        else:
                            check_transfer = False
                    except ValueError:
                        print()
                        print("> You must type a number. <")
                        print()

                # Check the password from the user's account.
                check_password = True
                attempts = 3
                while check_password:
                    password = input("Please type your password to confirm the transaction: ")
                    if attempts > 0:
                        if password != acc.password:
                            attempts -= 1
                            print()
                            print("> Wrong password ! Number the attempts left:", attempts, "<")
                            print()
                        else:
                            check_password = False
                    elif attempts == 0:
                        print()
                        print("> You have exceeded the number of attempts ! <")
                        print()
                        return [0, 0, 0]
                    else:
                        check_password = False
                print()
                current_date = datetime.datetime.now()
                formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
                print("You transfer", str(transfer_value), "to the account number", str(number), "at", formatted_date)
                
                # Return how much was transfered, the account's name and the record of the transaction, 
                # how much money was withdrawn and where it went. 
                return [transfer_value, number, formatted_date]
            else:
                print()
                print("> Account not found <")
                return [0,0,0]
        else:
            print()
            print("> Account not found <")
            return [0,0,0]
             
    def statement(self, balance, transactions):
        # Get the dictionary.
        operations = transactions
        acc_balance = balance
        
        print("#######################################")
        print("#                                     #")
        print("# Here's the transactions operations: #")
        print("#                                     #")
        print("#######################################")
        print()
    
        # Define a custom key function to extract the last date value of each element
        def get_last_date_value(key):
            # Check if the list exists and is not empty
            if key in operations and len(operations[key]) > 0:
                # Parse the date string into a datetime.datetime object
                date_string = operations[key][0][-1]
                date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
                return date_object
            # Return a default value for comparison
            return datetime.datetime.min
    
        # Sort the dictionary keys using the custom key function
        sorted_keys = sorted(operations.keys(), key=get_last_date_value)
        # Create a new dictionary to store the sorted values
        sorted_dict = {}
        for key in sorted_keys:
            sorted_dict[key] = operations[key]

        # Print the statment
        for key, value in sorted_dict.items():
            if key == "Transfered":
                trans = operations["Transfered"]
                print("--------------------------------------------------------------------")
                print("Transfer Operations: ")
                if len(trans) > 0:
                    for t in trans:
                        print("Transfered $ " + str(t[0]) + " to the account number " + str(t[1])+ " at " + str(t[2]))
                else:
                    print("No Transfer Operations")
                print("--------------------------------------------------------------------")
                print()
            elif key == "Deposited":
                dep = operations["Deposited"]
                print("--------------------------------------------------------------------")
                print("Deposit Operations: ")
                if len(dep) > 0:
                    for d in dep:
                        print("Deposited $ " + str(d[0]) + " at " + str(d[1]))
                else:
                    print("No Deposit Operations")
                print("--------------------------------------------------------------------")
                print()
            elif key == "Withdrawn":
                wit = operations["Withdrawn"]
                print("--------------------------------------------------------------------")
                print("Withdraw Operations: ")
                if len(wit) > 0:
                    for w in wit:
                        print("Withdraw $ " + str(w[0]) + " at " + str(w[1]))
                else:
                    print("No Withdraw Operations")
                print("--------------------------------------------------------------------")
                print()
            elif key == "Received":
                rec = operations["Received"]
                print("--------------------------------------------------------------------")                
                print("Received Operations: ")
                if len(rec) > 0:
                    for r in rec:
                        print("Receive $ " + str(r[0]) + " from the account number " + str(r[1]) + " at " + str(r[2]))
                else:
                    print("No Received Operations")
                print("--------------------------------------------------------------------")
                print()
        print("-------------------------")
        print("Balance: $" + str(balance))
        print("-------------------------")
        print()
        print("--------------------------------------------------------------------")
        
def running(accounts):
    # Creates the object for the operations.
    operation = Operation()
    
    # Creates accounts from the dataset.
    sample = accounts
    bank_accounts = []
    for i in range(len(sample["name"])):
        accs = Account(sample["name"][i], sample["agency"][i], sample["number"][i], sample["password"][i], sample["balance"][i], sample["transactions"][i])
        bank_accounts.append(accs)
        
    # Main Menu.
    print("#######################")
    print("#                     #")
    print("#  Welcome to PyBank  #")
    print("#                     #")
    print("#######################")
    print()
    
    # Check the user input.            
    quit_menu = False
    while not quit_menu:
        print("> Select one of the options <")
        user_access = input("Type A to access your account, C to create an account, M to enter Manager Mode or E to exit: ")
        print()
        # Guarantees that the input is capitalize.     
        user_access = user_access.capitalize()
        
        # Create an account
        if user_access == "C":
            acc = operation.create_account()
            sample["name"].append(acc.name)
            sample["password"].append(acc.password)
            sample["number"].append(acc.number)
            sample["agency"].append(acc.agency)
            sample["balance"].append(acc.balance)
            sample["transactions"].append(acc.transactions)
            bank_accounts.append(acc)
            
        # Access an account
        elif user_access == "A":
            # Get the account number
            account_number = operation.access_account(sample)
            # Retrieve the value if the account number is not zero the account is in the data base.
            in_account = True
            if account_number == 0:
                in_account = False
                
            # Operations loop
            while in_account:
                # Get the account from the account number
                for bank_account in bank_accounts:
                    if account_number == bank_account.number:
                        acc = bank_account
                print()
                user_input = input("Type T for transfer, D for deposit, W for withdraw, S to check your statement or Q to exit: ").capitalize()
                user_input = user_input.capitalize()
                print()
                # Transfer
                if user_input == "T":
                    transfer_to = operation.transfer(sample, acc)
                    transfer_value = transfer_to[0]
                    transfer_number = transfer_to[1]
                    transfer_date = transfer_to[2]
                    for target_acc in bank_accounts:
                        if transfer_number == target_acc.number:
                            target_acc.balance += float(transfer_value)
                            acc.balance -= float(transfer_value)
                            target_acc.transactions["Received"].append([transfer_value, acc.number, transfer_date])
                            acc.transactions["Transfered"].append([transfer_value, transfer_number, transfer_date])
                # Deposit
                elif user_input == "D":
                    deposit = operation.deposit()
                    acc.balance += deposit[0]
                    acc.show_statement(acc.agency, acc.number, acc.balance)
                    acc.transactions["Deposited"].append([float(deposit[0]), deposit[1]])
                # Withdraw
                elif user_input == "W":
                    withdraw = operation.withdraw(acc)
                    if withdraw[0] != 0 and withdraw[1] != 0:
                        acc.balance -= withdraw[0]
                        acc.transactions["Withdrawn"].append([float(withdraw[0]), withdraw[1]])
                # Statement
                elif user_input == "S":
                    operation.statement(acc.balance, acc.transactions)
                # Quit
                elif user_input == "Q":
                    in_account = False
                    
        # Manager Mode
        elif user_access == "M":
            total_bank_balance = 0
            for bank_account in bank_accounts:
                bank_account.show_informations(bank_account.name, bank_account.agency, bank_account.number, bank_account.password, bank_account.balance)
                operation.statement(bank_account.balance, bank_account.transactions)
                total_bank_balance += bank_account.balance

            print("--------------------------------------------------------------------")
            print("The total money in the bank is", total_bank_balance)
            print("--------------------------------------------------------------------")
            print()
        # Exit
        elif user_access == "E":
            print("You've exited")
            print("Thanks for coming")
            print()
            quit_menu = True
        
running(accounts)
