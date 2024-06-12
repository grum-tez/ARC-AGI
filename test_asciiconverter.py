import unittest
import json
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
                "ascii_art": " *#\n@%&\nO$X"
            },
            {
                "array": [
                    [1, 1, 1],
                    [2, 2, 2],
                    [3, 3, 3]
                ],
                "ascii_art": "***\n###\n@@@"
            }
        ]

    def extract_sample_arrays(self, json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        arrays = []
        for element in data['train']:
            arrays.append(element['input'])
            arrays.append(element['output'])
        
        for element in data['test']:
            arrays.append(element['input'])
            arrays.append(element['output'])
        
        return arrays

    def test_convert_back(self):
        for case in self.test_cases:
            with self.subTest(case=case):
                self.assertEqual(convert_back(case["ascii_art"]), case["array"])

    def convert_and_back(self, array):
        ascii_art = array_to_ascii_art(array)
        converted_back_array = convert_back(ascii_art)
        return {
            "original_array": array,
            "ascii_art": ascii_art,
            "converted_back_array": converted_back_array
        }

    def check_matrix(self, array):
        result = self.convert_and_back(array)
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
        return summary
        # Hardcoded first input matrix from the JSON file
        original_array = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 6, 6, 0, 6, 6, 0],
            [0, 6, 0, 0, 0, 6, 0],
            [0, 6, 6, 6, 6, 6, 0]
        ]
        self.check_matrix(original_array)

    def test_hardcoded_json_conversion_2(self):
        # Hardcoded second input matrix from the JSON file
        original_array = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 7, 7, 7, 7],
            [0, 0, 0, 0, 7, 0, 0, 0, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 7, 0, 0, 0, 7],
            [0, 0, 0, 0, 7, 7, 7, 7, 7]
        ]

        ascii_art = array_to_ascii_art(original_array)
        converted_back_array = convert_back(ascii_art)

        self.assertEqual(original_array, converted_back_array)

    def test_hardcoded_json_conversion_3(self):
        # Hardcoded third input matrix from the JSON file
        original_array = [
            [3, 3, 3, 3, 3, 3],
            [3, 0, 0, 0, 0, 3],
            [3, 0, 0, 0, 0, 3],
            [3, 3, 0, 0, 3, 3],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        ascii_art = array_to_ascii_art(original_array)
        converted_back_array = convert_back(ascii_art)
        self.assertEqual(original_array, converted_back_array)

    def test_sample_arrays_conversion(self):
        arrays = self.extract_sample_arrays('data/training/aba27056.json')
        summary = self.check_matrix_array(arrays)
        print("Summary:", summary)
        # Hardcoded fourth input matrix from the JSON file
        # original_array = [
        #     [0, 2, 2, 2, 2, 0, 0, 0, 0, 0],
        #     [0, 2, 0, 0, 2, 0, 0, 0, 0, 0],
        #     [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        #     [0, 2, 0, 0, 2, 0, 0, 0, 0, 0],
        #     [0, 2, 2, 2, 2, 0, 0, 0, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # ]

        # ascii_art = array_to_ascii_art(original_array)

        # converted_back_array = convert_back(ascii_art)

        # self.assertEqual(original_array, converted_back_array)

if __name__ == "__main__":

    unittest.main()
