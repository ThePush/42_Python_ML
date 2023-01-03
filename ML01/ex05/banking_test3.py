from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    acc_valid_1 = Account('Sherlock Holmes',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=1000.0)
    acc_valid_2 = Account('James Watson',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=25000.0,
                          info=None)

    acc_invalid_4 = Account("Douglass",
                            zip='42',
                            addr='boulevard bessieres',
                            value=42)
    acc_invalid_1 = Account("Adam",
                            value=42,
                            zip='0',
                            addr='Somewhere')
    acc_invalid_2 = Account("Bender Bending Rodríguez",
                            zip='1',
                            addr='Mexico')
    acc_invalid_3 = Account("Charlotte",
                            zip='2',
                            addr='Somewhere in the Milky Way',
                            value=42)
    acc_invalid_5 = Account("Edouard",
                            zip='3',
                            b='42',
                            e='42',
                            addr='France',
                            value=42)

    bank.add(acc_valid_1)
    bank.add(acc_valid_2)
    bank.add(acc_invalid_1)
    bank.add(acc_invalid_2)
    bank.add(acc_invalid_3)
    bank.add(acc_invalid_4)
    bank.add(acc_invalid_5)

# print a serie of tests with different error and success cases, using fix_account

    print('Transfer from valid to invalid')
    if bank.transfer('Sherlock Holmes', 'James Watson', 1000.0) is False:
        print('Failed')
        # account has an even number of attributes
        print('Fixing account')
        bank.fix_account('James Watson')
    if bank.transfer('Sherlock Holmes', 'James Watson', 1000.0) is False:
        print('Failed')
    else:
        print('Success')

    print('Transfer too much')
    if bank.transfer('James Watson', 'Sherlock Holmes', 100000.0) is False:
        print('Failed')
    else:
        print('Success')

    print('Transfer from invalid to valid')
    if bank.transfer('Edouard', 'Charlotte', 10.0) is False:
        print('Failed')
        # account has an attribute beginning with 'b'
        print('Fixing account')
        bank.fix_account('Edouard')
    if bank.transfer('Edouard', 'Charlotte', 10.0) is False:
        print('Failed')
    else:
        print('Success')