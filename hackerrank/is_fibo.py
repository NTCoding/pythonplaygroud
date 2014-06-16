# https://www.hackerrank.com/challenges/is-fibo - Level: Medium
import unittest
from ddt import data,ddt

@ddt
class Is_fibo_checker_specs(unittest.TestCase):

	@data(1, 2, 3, 5, 8, 13, 21, 89, 144, 233, 987, 10946)
	def test_correctly_identifies_fibonnaci_numbers(self, fibonacci_number):
		checker = IsFiboChecker()
		result =  checker.is_fibo(fibonacci_number)
		self.assertEqual(result, "IsFibo")

	@data(0, 4, 6, 20, 87, 143, 145, 187, 200, 754, 966, 986, 10947)
	def test_correctly_identifies_non_fibonacci_numbers(self, non_fibonacci_number):
		checker = IsFiboChecker()
		result = checker.is_fibo(non_fibonacci_number)
		self.assertEqual(result, "IsNonFibo")

# end of tests

# solution - submit this
import sys

class IsFiboChecker:

	def is_fibo(self, number):
		if number == 0: 
			return "IsNonFibo"
		else:	
			return self.__is_fibo(number, [1, 2])

	def __is_fibo(self, number, last_fibs):
		if number in last_fibs: 
			return "IsFibo"
		elif number < last_fibs[1]:
			return "IsNonFibo"
		else:
			next_fib = sum(last_fibs)
			new_fibs = [last_fibs[1], next_fib]
			return self.__is_fibo(number, new_fibs)


#unittest.main()
lines = sys.stdin.readlines()[1:]
nums = [ int(l) for l in lines ]
checker = IsFiboChecker()
[ print(checker.is_fibo(n)) for n in  nums ]
