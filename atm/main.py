import insert_card
import pin_number
import select_account
import balance

def main():
    card_number = insert_card.InsertCard()

    pin = input("write pin number: ")
    print(pin)
    if pin_number.PinNumber().check_pin_number(pin, card_number):
        pass
    else:
        print("false pin number")
        return False
    
    accounts = select_account.SelectAccount()
    accounts_number = accounts.get_account(card_number)
    print(accounts_number)
    account_index = input("select account index. (It starts 0): ")
    account_number = ""
    if accounts.select_accounts(int(account_index)) == False:
        print("false selected account")
        return False
    else:
        account_number = accounts.select_accounts(int(account_index))
    
    balanceOperation = balance.Balance(account_number)
    purpose = input("select number. (1: see balance, 2: withdraw, 3: diposit ): ")
    if purpose == "1":
        return balanceOperation.getBalance(account_number)
    elif purpose == "2":
        withdraw_money = int(input("write money: "))
        return balanceOperation.withdraw(account_number,withdraw_money)
    elif purpose == "3":
        deposit_money = int(input("write money: "))
        return balanceOperation.deposit(account_number,deposit_money)
    else:
        print("false selected transaction")
        return False

if __name__ == '__main__':
    last_money = main()
    print(last_money)
