import unittest
from ddt import ddt,data

@ddt
class Roman_numerals_kata_specs(unittest.TestCase):
	
	@data((1, "I"), (2, "II"), (3, "III"), (4, "IV"), 
		  (5, "V"), (6, "VI"), (7, "VII"), (8, "VIII"),(9, "IX"))
	def test_converts_single_digits_to_equivalent_numerals(self, value):
		number,numeral = value
		converter = RomanNumeralConverter()
		converted = converter.convert(number)
		self.assertEqual(converted, numeral)

	@data((10, "X"), (11, "XI"), (12, "XII"), (13, "XIII"), (20, "XX"), 
		  (25, "XXV"), (32, "XXXII"), (49, "XLIX"), (50, "L"), (51, "LI"), 
		  (55, "LV"), (74, "LXXIV"), (75, "LXXV"), (91, "XCI"), (99, "XCIX"))
	def test_converts_double_digits_to_equivalent_numerals(self, value):
		number,numeral = value
		converter = RomanNumeralConverter()
		converted = converter.convert(number)
		self.assertEqual(converted, numeral)

	@data((100, "C"), (101, "CI"), (151, "CLI"), (349, "CCCXLIX"), 
		  (487, "CDLXXXVII"), (500, "D"), (633, "DCXXXIII"), (999, "CMXCIX"))
	def test_converts_triple_digits_to_equivalent_numerals(self, value):
		number,numeral = value
		converter = RomanNumeralConverter()
		converted = converter.convert(number)
		self.assertEqual(converted, numeral)
'''
	@data((1000, "M"), (3000, "MMM"), (4001, "MMMMI"), (5126, "MMMMMCXXVI"), 
		  (9067, "MMMMMMMMMLXVII"), (9998, "MMMMMMMMMCMXCVIII"), 
		  (7553, "MMMMMMMDLIII"), (6244, "MMMMMMCCXLIV"))
	def test_converts_quadruple_digits_to_equivalent_numerals(self, value):
		number,numeral = value
		converter = RomanNumeralConverter()
		converted = converter.convert(number)
		self.assertEqual(converted, numeral)

	@data((10000, "MMMMMMMMMM"), 
		  (500001, "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMI"), 
		  (235123, "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCXXIII"))
	def test_converts_gigantic_numbers_to_equivalent_numerals(self, value):
		number,numeral = value
		converter = RomanNumeralConverter()
		converted = converter.convert(number)
		self.assertEqual(converted, numeral)
'''

class RomanNumeralConverter:

	def convert(self, number):
		# input magnitude will soon come into play
		hundredsX = int(number / 100)
		tensX = int((number - (hundredsX * 100)) / 10)
		unitsX = (number - (hundredsX * 100) - (tensX * 10))
		hundreds = self.__hundredsFor(hundredsX) 
		tens = self.__tensFor(tensX) 
		units = self.__unitsFor(unitsX)
		return hundreds + tens + units

	def __hundredsFor(self, number):
		if (number == 9): return "CM"
		elif (number == 4): return "CD"
		elif (number == 5): return "D"
		elif (number > 5): return "D" + ("C" * (number - 5))
		elif (number == 0): return ""
		else: return "C" * number

	def __tensFor(self, number):
		if (number == 9): return "XC"
		elif (number == 4): return "XL"
		elif (number == 5): return "L"
		elif (number > 5): return "L" + ("X" * (number - 5))
		elif (number == 0): return ""
		else: return "X" * number
		
	def __unitsFor(self, number):
		if (number == 9): return "IX"
		if (number == 4): return "IV"
		elif (number == 5): return "V"
		elif (number > 5): return "V" + ("I" * (number - 5))
		elif (number == 0): return ""
		else: return "I" * number

	


unittest.main()



