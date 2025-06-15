class BankAccount:
  def __init__(self, initial_balance= 0):
    self.account_balance = initial_balance

  def deposit(self,amount):
    if amount > 0:
      self.account_balance += amount
      print (f"You deposited{amount}. Balnce is now{self.account_balance}")

  def withdraw(self,amount):
     if amount <= self.account_balance:
        self.account_balance -= amount
        print(f"Withdrew: ${amount:.2f}")
        return True
     else:
        print("Insufficient funds. Withdrawal denied.")
        return False
     
  def display_balance(self):
    print(f"Current balance: ${self.account_balance:.2f}")