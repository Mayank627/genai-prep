# Python doesn't have strict encapsulation like public/private for C++/Java, 
# but we can use naming conventions to indicate that certain attributes or methods are intended to be private.

class Bank:
    def __init__(self, balance):
        self.balance = balance
        self._pin = 1234  #protected attribute; convention
        self.__secret_code = "XYZ" #private attribute; name mangling

bank = Bank(1000)
print(bank.balance)
        