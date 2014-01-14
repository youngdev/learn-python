#!/usr/bin/env python

import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):

	def test_numeroSimples(self):
		self.assertEqual(FizzBuzz(1), 1)
		self.assertEqual(FizzBuzz(2), 2)
		self.assertEqual(FizzBuzz(4), 4)


	def test_Fizz(self):
		self.assertEqual(FizzBuzz(3), "fizz")
		self.assertEqual(FizzBuzz(9), "fizz")

	def test_Buzz(self):
		self.assertEqual(FizzBuzz(5), "buzz")
		self.assertEqual(FizzBuzz(10), "buzz")

	def test_FizzBuzz(self):
		self.assertEqual(FizzBuzz(15), "fizzbuzz")
		self.assertEqual(FizzBuzz(30), "fizzbuzz")


if __name__ == '__main__':
	unittest.main()