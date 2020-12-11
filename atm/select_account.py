class SelectAccount:
    def __init__(self):
        account_number = []
        pass

    def select_accounts(self, account_index):
        if account_index < 0:
            return False
        if account_index < len(self.account_number):
            return self.account_number[account_index]
        else:
            return False
        
    def get_account(self,card_number):
        self.account_number = ["1111-1111-1111-1111","2222-2222-2222-222"]
        return self.account_number