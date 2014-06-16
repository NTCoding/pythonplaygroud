# https://www.hackerrank.com/challenges/utopian-tree - Level: EASY
import unittest
import sys
from ddt import ddt,data

@ddt
class utopian_tree_integration_specs(unittest.TestCase):

	@data((["2", "0", "1"], [1,2]), (["2","3","4"], [6,7]))
	def test_calculates_height_after_n_cycles_by_doubling_during_monsoon_and_adding_1_in_summer(self, value):
		input_lines, new_heights = value
		input_stream = StubInputStream(input_lines)
		calc = TreeHeightCalculationService(InstructionsParser(), TreeHeightCalculator())
		result = calc.calculate(input_stream)
		self.assertEqual(result, new_heights)


@ddt
class instruction_parser_specs(unittest.TestCase):

	@data( (["2", "0", "1"], [0, 1]), (["1", "5"], [5]), (["2", "3", "4"], [3,  4]) )
	def test_uses_first_line_to_work_out_how_many_seasons_and_converts_each_season_to_integer(self, values):
		input_lines,number_of_seasons = values
		stream = StubInputStream(input_lines)
		parser = InstructionsParser()
		result = parser.parseFrom(stream)
		self.assertEqual(result, number_of_seasons)


@ddt 
class tree_height_calculator_specs(unittest.TestCase):

	@data( (0, 1), (1, 2), (3, 6), (4, 7) )
	def test_calculates_new_height_by_doubling_during_monsoons_and_increasing_by_1_in_summer(self, value):
		num_seasons,new_height = value
		calc = TreeHeightCalculator()
		result = calc.calculate(num_seasons)
		self.assertEqual(result, new_height)


class StubInputStream:

	def __init__(self, lines):
		self.lines = lines

	def readlines(self): return self.lines

# End of tests ^^ 

# Start of solution - only submit this
import sys

class TreeHeightCalculationService:

	def __init__(self, parser, calculator):
		self.parser = parser
		self.calculator = calculator

	def calculate(self, stream):
		return [ self.calculator.calculate(n) for n in self.parser.parseFrom(stream)]


class InstructionsParser:

	def __init__(self):
		""

	def parseFrom(self, stream):
		lines = stream.readlines()
		return [ int(n) for n in lines[1:] ]


class TreeHeightCalculator:

	def __init__(self):
		""

	def calculate(self, num_seasons):
		height = 1
		for n in range(1, num_seasons + 1):
			if (n % 2) == 1:
				height = height * 2
			else: 
				height += 1
		return height


#unittest.main()
calc = TreeHeightCalculationService(InstructionsParser(), TreeHeightCalculator())
result = calc.calculate(sys.stdin)
[ print(r) for r in result ]
