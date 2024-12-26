class Account:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")


    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")


    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = []


    def add_account(self, account):
        self.accounts.append(account)


    def get_accounts(self):
        return self.accounts


    def __str__(self):
        return f"Customer [Name: {self.name}, ID: {self.customer_id}]"


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []


    def add_customer(self, customer):
        self.customers.append(customer)


    def get_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None


    def __str__(self):
        return f"Bank [Name: {self.name}]"


# Example usage
# Create a bank
bank = Bank("National Bank")


# Create customers
customer1 = Customer("Ram", 1)
customer2 = Customer("Sita", 2)


# Add customers to the bank
bank.add_customer(customer1)
bank.add_customer(customer2)


# Create accounts for customers
account1 = Account("ACC1001", 500)
account2 = Account("ACC1002", 1000)


# Add accounts to customers
customer1.add_account(account1)
customer2.add_account(account2)


# Perform operations
account1.deposit(200)
account1.withdraw(100)
print(f"Balance for {customer1.name}: {account1.get_balance()}")


account2.deposit(500)
account2.withdraw(300)
print(f"Balance for {customer2.name}: {account2.get_balance()}")


# Print customer details
print(customer1)
print(customer2)


# Print bank details
print(bank)
