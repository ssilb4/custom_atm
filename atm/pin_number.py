class PinNumber:
    def __init__(self):
        pin_number =  ""
    
    def get_user_number(self, pin_number):
        return pin_number
    
    def get_pin_number(self, card_number):
        # pass card_number and get pin _number
        return "1234"

    def check_pin_number(self, pin_number, card_number):
        if self.get_pin_number(card_number) == self.get_user_number(pin_number):
            return True
        else:
            return False