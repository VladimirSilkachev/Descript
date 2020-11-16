class Value:
    def __get__(self, obj, obj_type):
        self.commission = obj.commission
        return self

    def __set__(self, obj, value):
        self.value = value
        return self

    def __repr__(self):
        return str((1 - self.commission) * self.value)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.3)
new_account.amount = 120
print(new_account.amount)
