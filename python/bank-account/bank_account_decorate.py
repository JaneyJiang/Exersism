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
    
    def is_open(func):
        def wrapped(self, *args):
            if self._isOpen == False:
                raise ValueError(BankClosedMsg)
            return func(self,*args)
        return wrapped

    @is_open
    def get_balance(self):
        return self._balance

    def open(self):
        if self._isOpen == False:
            self._isOpen = True
            self._balance = 0
        else:
            raise ValueError(BankAlreadyOpenMsg)

    @is_open
    def deposit(self, amount):
        if amount > 0:
            with self._balance_lock:
                self._balance += amount
        else:
            raise ValueError(MoneyAccountInputErr)
        
    @is_open
    def withdraw(self, amount):
        if amount <= self._balance and amount > 0:
            with self._balance_lock:
                self._balance -= amount
        else:
            raise ValueError(MoneyAccountInputErr)

    @is_open
    def close(self):
        self._isOpen = False