#!/usr/bin/env python
# encoding: utf-8

import unittest
from loan_calculator import loan_calculator

class LoanCalculator(unittest.TestCase):
    def test_month_is_not_greater_than_twelve(self):
        self.assertEquals(calculate_repayable(10000,13,13),"Invalid number of months")
    def test_for_correct_result(self):
        self.assertEquals(calculate_repayable(100000,12,112000))
