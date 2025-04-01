'''
Homework1
Name:Drake Pierce-Demksi
github link:
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account:
    """
    A simple bank account class that supports deposits, withdrawals, and balance checks.
    
    Attributes:
        name (str): The name of the account holder.
        balance (float): The current balance of the account.
    """
    
    def __init__(self, name, starting_amount):
        """
        Initializes a Bank_Account instance with a name and a starting balance.
        
        Args:
            name (str): The account holder's name.
            starting_amount (float): The initial balance of the account.
        """
        self.name = name  # Store account holder's name
        self.balance = float(starting_amount)  # Store account balance as a float

    def __repr__(self):
        """
        Returns an unambiguous string representation of the Bank_Account object.
        
        Returns:
            str: A string in the format "Bank_Account(name='Name', Account Balance=Balance)".
        """
        return f"Bank_Account(name='{self.name}', Account Balance={self.balance:.2f})"
    
    def __str__(self):
        """
        Returns a user-friendly string representation of the Bank_Account object.
        
        Returns:
            str: A string displaying the account name and balance.
        """
        return f"Account Name: {self.name}\nAccount Balance: {self.balance:.2f}"
    
    def deposit(self, amount):
        """
        Deposits a specified amount into the account if it is greater than zero.
        
        Args:
            amount (float): The amount to be deposited.
        
        Returns:
            str: A message indicating the success or failure of the deposit.
        """
        if amount > 0:
            self.balance += amount  # Increase balance by deposit amount
            return f"{amount} deposited. New Balance: {self.balance:.2f}"
        else:
            return "Please deposit a positive number."
    
    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if the amount is greater than zero
        and does not exceed the available balance.
        
        Args:
            amount (float): The amount to be withdrawn.
        
        Returns:
            str: A message indicating the success or failure of the withdrawal.
        """
        if amount <= 0:
            return "Please withdraw an amount greater than zero."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount  # Decrease balance by withdrawal amount
            return f"{amount} withdrawn. New Balance: {self.balance:.2f}"
    
    def check_balance(self):
        """
        Returns the current balance of the account.
        
        Returns:
            str: A message displaying the account balance.
        """
        return f"Balance: {self.balance:.2f}"  # Return formatted balance string
    
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))  # Run doctest to verify implementation
