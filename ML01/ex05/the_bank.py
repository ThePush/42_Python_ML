class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    '''The bank'''

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        ''' Add new_account in the Bank
        @new_account: Account() new account to append
        @return
        True if success, False if an error occured
        '''
        if not isinstance(new_account, Account):
            return False
        if new_account.name in [account.name for account in self.accounts]:
            return False
        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        '''Perform the fund transfer
        @origin: str(name) of the first account
        @dest:
        str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return
        True if success, False if an error occured
        How do we define if a bank account is corrupted? A corrupted bank account has:
        • an even number of attributes,
        • an attribute starting with b,
        • no attribute starting with zip or addr,
        • no attribute name, id and value,
        • name not being a string,
        • id not being an int,
        • value not being an int or a float.
        '''
        if not isinstance(origin, str) or not isinstance(dest, str):
            return False
        if not isinstance(amount, (int, float)) or amount < 0:
            return False
        if origin not in [account.name for account in self.accounts]:
            return False
        if dest not in [account.name for account in self.accounts]:
            return False
        for account in self.accounts:
            if account.name == origin or account.name == dest:
                if len(account.__dict__) % 2 == 0:
                    return False
                if any([key.startswith('b') for key in account.__dict__]):
                    return False
                if not any([key.startswith('zip') or key.startswith('addr') for key in account.__dict__]):
                    return False
                if not hasattr(account, 'name') or not hasattr(account, 'id') or not hasattr(account, 'value'):
                    return False
                if not isinstance(account.name, str):
                    return False
                if not isinstance(account.id, int):
                    return False
                if not isinstance(account.value, (int, float)):
                    return False
        if dest == origin:
            return True
        for account in self.accounts:
            if account.name == origin:
                if account.value < amount:
                    return False
                account.transfer(-amount)
            if account.name == dest:
                account.transfer(amount)
        return True

    def fix_account(self, name):
        ''' fix account associated to name if corrupted
        @name:
        str(name) of the account
        @return True if success, False if an error occured
        recovers a corrupted account if it parameter name correspond to the
        attribute name of one of the account in accounts (attribute of Bank). If name is not a
        string or does not corresponded to an account name, the method return False.
        '''
        if not isinstance(name, str):
            return False
        if name not in [account.name for account in self.accounts]:
            return False
        for account in self.accounts:
            if account.name == name:
                for key in [key for key in account.__dict__ if key.startswith('b')]:
                    account.__dict__.pop(key)
                if not hasattr(account, 'name'):
                    account.name = name
                if not hasattr(account, 'id'):
                    account.id = account.ID_COUNT
                    Account.ID_COUNT += 1
                if not hasattr(account, 'value'):
                    account.value = 0
                if not any([key.startswith('zip') or key.startswith('addr') for key in account.__dict__]):
                    account.zip = '000-000'
                if len(account.__dict__) % 2 == 0:
                    setattr(account, 'odd', True)
        return True

# https://www.geeksforgeeks.org/python-dictionary-update-method/
# https://pythonexamples.org/python-kwargs/
# https://www.geeksforgeeks.org/python-hasattr-method/
