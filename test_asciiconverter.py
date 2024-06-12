import unittest
from asciiconverter import array_to_ascii_art, convert_back

class TestAsciiConverter(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {
                "array": [
                    [0, 1, 2],
                    [3, 4, 5],
                    [6, 7, 8]
                ],
                "ascii_art": " *#\n@%&\nO$X\n"
            },
            {
                "array": [
                    [1, 1, 1],
                    [2, 2, 2],
                    [3, 3, 3]
                ],
                "ascii_art": "***\n###\n@@@\n"
            }
        ]

    def test_array_to_ascii_art(self):
        for case in self.test_cases:
            with self.subTest(case=case):
                self.assertEqual(array_to_ascii_art(case["array"]), case["ascii_art"])

    def test_convert_back(self):
        for case in self.test_cases:
            with self.subTest(case=case):
                self.assertEqual(convert_back(case["ascii_art"]), case["array"])

if __name__ == "__main__":
    unittest.main()
