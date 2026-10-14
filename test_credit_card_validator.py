import unittest

from credit_card_validator import (
    get_card_type,
    has_valid_length,
    is_valid,
    make_single_digit,
    sum_of_doubled_digits,
    sum_of_odd_place_digits,
)


class TestCardType(unittest.TestCase):
    def test_visa(self):
        self.assertEqual("Visa", get_card_type("4388576018410707"))

    def test_mastercard(self):
        self.assertEqual("MasterCard", get_card_type("5555555555554444"))

    def test_american_express(self):
        self.assertEqual("American Express", get_card_type("378282246310005"))

    def test_discover(self):
        self.assertEqual("Discover", get_card_type("6011111111111117"))

    def test_unknown(self):
        self.assertEqual("Unknown", get_card_type("9111111111111111"))


class TestLength(unittest.TestCase):
    def test_too_short(self):
        self.assertFalse(is_valid("411111111111"))

    def test_too_long(self):
        self.assertFalse(is_valid("41111111111111111"))

    def test_thirteen_digits_allowed(self):
        self.assertTrue(has_valid_length("4222222222222"))


class TestBadInput(unittest.TestCase):
    def test_letters_in_number(self):
        self.assertFalse(is_valid("4677@6778300)6336"))

    def test_empty_string(self):
        self.assertFalse(is_valid(""))


class TestLuhnSteps(unittest.TestCase):
    def test_doubled_digits_sum(self):
        self.assertEqual(37, sum_of_doubled_digits("673978708778689"))

    def test_odd_place_sum(self):
        self.assertEqual(38, sum_of_odd_place_digits("5676875678788978"))

    def test_single_digit_of_12(self):
        self.assertEqual(3, make_single_digit(12))

    def test_single_digit_of_7(self):
        self.assertEqual(7, make_single_digit(7))


class TestValidity(unittest.TestCase):
    def test_pdf_invalid_example(self):
        self.assertFalse(is_valid("4512325432"))

    def test_pdf_valid_example(self):
        self.assertTrue(is_valid("875986808088"))

    def test_valid_mastercard(self):
        self.assertTrue(is_valid("298398239832"))

    def test_valid_american_express(self):
        self.assertTrue(is_valid("37828254644784"))

    def test_valid_discover(self):
        self.assertTrue(is_valid("5734849849804804"))

    def test_right_start_but_fails_luhn(self):
        self.assertFalse(is_valid("5446743643874879"))


