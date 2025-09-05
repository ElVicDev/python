""" Día 43: Encapsulación
Implementar la encapsulación en una clase. """

class BankAccount:
    """Clase que representa una cuenta bancaria con encapsulación."""
    def __init__(self, account_holder, balance=0):
        self.__account_holder = account_holder  # Atributo privado
        self.__balance = balance                  # Atributo privado

    def deposit(self, amount):
        """Deposita una cantidad en la cuenta."""
        if amount > 0:
            self.__balance += amount
            return f"Deposited: ${amount:.2f}. New balance: ${self.__balance:.2f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """Retira una cantidad de la cuenta si hay fondos suficientes."""
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrew: ${amount:.2f}. New balance: ${self.__balance:.2f}"
            else:
                return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def get_balance(self):
        """Devuelve el saldo actual de la cuenta."""
        return f"Current balance: ${self.__balance:.2f}"
    
    def get_account_holder(self):
        """Devuelve el nombre del titular de la cuenta."""
        return self.__account_holder
    
# Crear una instancia de BankAccount
account = BankAccount("Alice", 100)
print(account.get_balance())  # Saldo inicial
print(account.deposit(50))     # Depositar dinero
print(account.withdraw(30))    # Retirar dinero
print(account.withdraw(150))   # Intentar retirar más de lo disponible
print(account.get_balance())  # Saldo final
print(account.get_account_holder())  # Nombre del titular de la cuenta

# Salida esperada:
# Current balance: $100.00
# Deposited: $50.00. New balance: $150.00
# Withdrew: $30.00. New balance: $120.00
# Insufficient funds.
# Current balance: $120.00
# Alice