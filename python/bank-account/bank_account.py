import threading 
BankAlreadyOpenMsg = "The bank is already open！"
BankClosedMsg = "The bank is not open！"
BankAlreadyCloseMsg = "The bank is already closed！"
MoneyAccountInputErr = "Please check your input amount!"
class BankAccount(object):
    def __init__(self):
        self._isOpen = False
        self._balance = 0 
        self._balance_lock = threading.Lock()

    def get_balance(self):
        if self._isOpen:
            return self._balance
        else:
            raise ValueError(BankClosedMsg)

    def open(self):
        if self._isOpen == False:
            self._isOpen = True
            self._balance = 0
        else:
            raise ValueError(BankAlreadyOpenMsg)

    
    def deposit(self, amount):
        if self._isOpen:
            if amount > 0:
                with self._balance_lock:
                    self._balance += amount
            else:
                raise ValueError(MoneyAccountInputErr)
        else:
            raise ValueError(BankClosedMsg)

    def withdraw(self, amount):
        if self._isOpen:
            if amount <= self._balance and amount > 0:
                with self._balance_lock:
                    self._balance -= amount
            else:
                raise ValueError(MoneyAccountInputErr)
        else:
            raise ValueError(BankClosedMsg)

    def close(self):
        if self._isOpen:
            self._isOpen = False
        else:
            raise ValueError(BankAlreadyOpenMsg)