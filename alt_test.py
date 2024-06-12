import unittest
from altfunctions import convert_grid, convert_back_grid
from test_asciiconverter import TestAsciiConverter

class TestAltFunctions(unittest.TestCase):
    def test_basic_matrix_conversion(self):
        original_array = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected_ascii_art = "|*|#|@|\n---|---|---\n|%|&|O|\n---|---|---\n|$|X|~|"
        
        ascii_art = convert_grid(original_array)
        print("ORIGINAL ARRAY:")
        for row in original_array:
            print(row)
        print("ASCII ART:")
        print(ascii_art)
        print("EXPECTED")
        print(expected_ascii_art)
        print("RECREATED ARRAY:")
        for row in convert_back_grid(ascii_art):
            print(row)
        # self.assertEqual(ascii_art, expected_ascii_art)
        
        converted_back_array = convert_back_grid(ascii_art)
        self.assertEqual(converted_back_array, original_array)

    def check_matrix(self, array):
        result = TestAsciiConverter().convert_and_back(array, conversion_method="grid")
        if result["original_array"] != result["converted_back_array"]:
            print("ORIGINAL ARRAY:")
            for row in result["original_array"]:
                print(row)
            print("ASCII ART STRING:", result["ascii_art"])
            print("RESTORED ARRAY:")
            for row in result["converted_back_array"]:
                print(row)
        return result["original_array"] == result["converted_back_array"]

    def check_matrix_array(self, arrays):
        summary = {"True": 0, "False": 0}
        for array in arrays:
            if self.check_matrix(array):
                summary["True"] += 1
            else:
                summary["False"] += 1
        assert summary["False"] == 0, f"Found {summary['False']} matrices that failed conversion."
        return summary

if __name__ == "__main__":
    unittest.main()
