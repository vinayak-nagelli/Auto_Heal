class ATMUser:
    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.__pin = pin  # Private variable for security
        self.balance = balance
        self.is_authenticated = False

    def verify_pin(self, entered_pin):
        if entered_pin == self.__pin:
            self.is_authenticated = True
            return True
        return False

    def get_balance(self):
        if not self.is_authenticated:
            return "Authentication Required"
        return self.balance

    def deposit(self, amount):
        if not self.is_authenticated:
            return "Authentication Required"
        if amount <= 0:
            return "Invalid Amount"
        
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.is_authenticated:
            return "Authentication Required"
        if amount <= 0:
            return "Invalid Amount"
        if amount > self.balance:
            return "Insufficient Funds"
        
        self.balance -= amount
        return self.balance

    def logout(self):
        self.is_authenticated = False
        return True