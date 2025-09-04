""" Día 42: Métodos de clase
Cree una clase para una cuenta bancaria con métodos de depósito y retiro. """

class BankAccount:
    """Clase que representa una cuenta bancaria."""
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposita una cantidad en la cuenta."""
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Retira una cantidad de la cuenta si hay fondos suficientes."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}"
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        """Devuelve el saldo actual de la cuenta."""
        return f"Current balance: ${self.balance:.2f}"
    
# Crear una instancia de BankAccount
account = BankAccount("Alice", 100)
print(account.get_balance())  # Saldo inicial
print(account.deposit(50))     # Depositar dinero
print(account.withdraw(30))    # Retirar dinero
print(account.withdraw(150))   # Intentar retirar más de lo disponible
print(account.get_balance())  # Saldo final

# Salida esperada:
# Current balance: $100.00
# Deposited: $50.00. New balance: $150.00
# Withdrew: $30.00. New balance: $120.00
# Insufficient funds.
# Current balance: $120.00