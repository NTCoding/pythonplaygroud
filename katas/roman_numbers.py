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

	@data((10, "I"), (11, "XI"), (12, "XII"), (13, "XIII"), (20, "XX"), 
		  (25, "XXV"), (32, "XXXII"), (49, "XLIX"), (50, "L"), (51, "LI"), 
		  (55, "LV"), (74, "LXXIV"), (75, "LXXV"), (91, "XCI"), (99, "XCIX"))
	def test_converts_double_digits_to_equivalent_numerals(self, value):
		number,numeral = value
		converter = RomanNumeralConverter()
		converted = converter.convert(number)
		self.assertEqual(converted, numeral)

	@data((100, "C"), (101, "CI"), (151, "CLI"), (349, "CCCXLIX"), 
		  (487, "CDLXXXVII"), (500, "D"), (633, "DCXXIII"), (999, "CMXCIX"))
	def test_converts_triple_digits_to_equivalent_numerals(self, value):
		number,numeral = value
		converter = RomanNumeralConverter()
		converted = converter.convert(number)
		self.assertEqual(converted, numeral)

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

class RomanNumeralConverter:

	def convert(self, number):
		return "ABC"

unittest.main()



