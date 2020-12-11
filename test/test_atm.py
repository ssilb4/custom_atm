import unittest

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from atm import insert_card
from atm import pin_number
from atm import select_account
from atm import balance


class TestAtm(unittest.TestCase):
    def test_insert_card(self):
        self.assertEqual(insert_card.InsertCard().insert_card(),"1111-1111-1111-1111")
        self.assertNotEqual(insert_card.InsertCard().insert_card(),"1111-1111-1111-1112")
    
    def test_pin_number(self):
        self.assertEqual(pin_number.PinNumber().get_user_number("5678"),"5678")
        self.assertNotEqual(pin_number.PinNumber().get_user_number("5678"),"157134")

        self.assertEqual(pin_number.PinNumber().get_pin_number("1111-1111-1111-1111"),"1234")
        self.assertEqual(pin_number.PinNumber().get_pin_number("1111-1111-1111-1112"),"1234")
        self.assertNotEqual(pin_number.PinNumber().get_pin_number("1111-1111-1111-1111"),"45623")
        self.assertNotEqual(pin_number.PinNumber().get_pin_number("1111-1111-1111-1112"),"1235")

        self.assertTrue(pin_number.PinNumber().check_pin_number("1234","1111-1111-1111-1111"))
        self.assertTrue(pin_number.PinNumber().check_pin_number("1234","1111-1423-7689-1131"))
        self.assertFalse(pin_number.PinNumber().check_pin_number("3456","1111-1423-7689-1131"))
        self.assertFalse(pin_number.PinNumber().check_pin_number("1236","1111-1423-7689-1131"))

    def test_select_account(self):
        self.assertEqual(select_account.SelectAccount().get_account("1234"),["1111-1111-1111-1111","2222-2222-2222-222"])
        self.assertNotEqual(select_account.SelectAccount().get_account("1234"),["1111-1111-1111-1111","2222-2222-2222-222","123-123"])
        self.assertNotEqual(select_account.SelectAccount().get_account("1234"),["1111-1111-1111-1111"])
        self.assertNotEqual(select_account.SelectAccount().get_account("1234"),["123-123"])

        s = select_account.SelectAccount()
        s.get_account("test")
        self.assertFalse(s.select_accounts(-1))
        self.assertFalse(s.select_accounts(2))
        self.assertEqual(s.select_accounts(0),"1111-1111-1111-1111")
        self.assertNotEqual(s.select_accounts(1),"1111-1111-1111-1111")
        self.assertEqual(s.select_accounts(1),"2222-2222-2222-222")

    def test_balance(self):
        b = balance.Balance("123")
        self.assertEqual(b.getBalance("123"), 100)
        self.assertNotEqual(b.getBalance("123"), 110)
        self.assertFalse(b.getBalance("1234"))

        self.assertFalse(b.withdraw("123", 123))
        self.assertEqual(b.withdraw("123",77), 23)
        self.assertNotEqual(b.getBalance("123"), 100)
        self.assertEqual(b.getBalance("123"), 23)
        self.assertFalse(b.withdraw("1234", 1))

        self.assertEqual(b.deposit("123",177), 200)
        self.assertNotEqual(b.getBalance("123"), 100)
        self.assertEqual(b.getBalance("123"), 200)
        self.assertFalse(b.deposit("1234", 1))
        self.assertEqual(b.getBalance("123"), 200)

        self.assertEqual(b.withdraw("123",77), 123)


if __name__ == '__main__':
    unittest.main()