import unittest
from ddt import ddt, data

@ddt
class Fibonacci_test_case(unittest.TestCase):
	
	@data( (22,21), (21,13), (145, 144), (55, 34), (54, 34) )
	def test_calculates_prevous_fibonnaci_number(self, value):
		number,fib = value
		calc = FibonacciCalculator()
		result = calc.calculatePrevious(number)
		self.assertEqual(result, fib)

	@data( (1, 2), (2, 3), (3, 5), (4, 5), (5, 8), (12, 13), (13,21) )
	def test_calculates_next_fibonnaci_number(self, value):
		number,fib = value
		calc = FibonacciCalculator()
		result = calc.calculateNext(number)
		self.assertEqual(result, fib)

class FibonacciCalculator:
	'''
	def calculatePrevious(self, number):
		# test for input less than 3
		nums = [1, 2]
		lastFib = 2
		while lastFib < number:
			lastFib = nums[0] + nums[1]
			nums[0] = nums[1]
			nums[1] = lastFib
		return nums[0]
	'''
	def calculatePrevious(self, target):
		return self.__calculatePrevious(target, [1,2])

	def __calculatePrevious(self, target, lastFibs):
		if (lastFibs[1] >= target):
			return lastFibs[0]
		else:
			nextFib = lastFibs[0] + lastFibs[1]
			fibs = [lastFibs[1], nextFib]
			return self.__calculatePrevious(target, fibs)

	def calculateNext(self, target):
		return self.__calculateNext(target, [1,2])

	def __calculateNext(self, target, lastFibs):
		if (lastFibs[1] > target):
			return lastFibs[1]
		else:
			nextFib = lastFibs[0] + lastFibs[1]
			fibs = [lastFibs[1], nextFib]
			return self.__calculateNext(target, fibs)


unittest.main()