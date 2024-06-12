import unittest
from altfunctions import convert_grid, convert_back_grid

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

if __name__ == "__main__":
    unittest.main()
