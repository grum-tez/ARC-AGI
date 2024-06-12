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
        for case in self.test_cases:
            with self.subTest(case=case):
                self.assertEqual(array_to_ascii_art(case["array"]), case["ascii_art"])

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
        self.assertEqual(result["original_array"], result["converted_back_array"])
        with open('data/training/0a938d79.json', 'r') as file:
            data = json.load(file)

        for element in data['train']:
            for key in ['input', 'output']:
                original_array = element[key]
                print("ORIGINAL ARRAY:")
                for row in original_array:
                    print(row)
                self.check_matrix(original_array)

        for element in data['test']:
            original_array = element['input']
            self.check_matrix(original_array)
    def test_hardcoded_json_conversion(self):
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
        print("ORIGINAL ARRAY:")
        for row in original_array:
            print(row)
        ascii_art = array_to_ascii_art(original_array)
        print("ASCII ART STRING:", ascii_art)
        converted_back_array = convert_back(ascii_art)
        print("RESTORED ARRAY:")
        for row in converted_back_array:
            print(row)
        self.assertEqual(original_array, converted_back_array)

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
        print("ORIGINAL ARRAY:")
        for row in original_array:
            print(row)
        ascii_art = array_to_ascii_art(original_array)
        print("ASCII ART STRING:", ascii_art)
        converted_back_array = convert_back(ascii_art)
        print("RESTORED ARRAY:")
        for row in converted_back_array:
            print(row)
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
        print("ORIGINAL ARRAY:")
        for row in original_array:
            print(row)
        ascii_art = array_to_ascii_art(original_array)
        print("ASCII ART STRING:", ascii_art)
        converted_back_array = convert_back(ascii_art)
        print("RESTORED ARRAY:")
        for row in converted_back_array:
            print(row)
        self.assertEqual(original_array, converted_back_array)

    def test_sample_arrays_conversion(self):
        arrays = self.extract_sample_arrays('data/training/aba27056.json')
        for i, original_array in enumerate(arrays):
            with self.subTest(i=i):
                print(f"Testing array {i}:")
                print("ORIGINAL ARRAY:")
                for row in original_array:
                    print(row)
                ascii_art = array_to_ascii_art(original_array)
                print("ASCII ART STRING:", ascii_art)
                converted_back_array = convert_back(ascii_art)
                print("RESTORED ARRAY:")
                for row in converted_back_array:
                    print(row)
                self.assertEqual(original_array, converted_back_array)
        # Hardcoded fourth input matrix from the JSON file
        original_array = [
            [0, 2, 2, 2, 2, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 2, 2, 2, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        print("ORIGINAL ARRAY:")
        for row in original_array:
            print(row)
        ascii_art = array_to_ascii_art(original_array)
        print("ASCII ART STRING:", ascii_art)
        converted_back_array = convert_back(ascii_art)
        print("RESTORED ARRAY:")
        for row in converted_back_array:
            print(row)
        self.assertEqual(original_array, converted_back_array)

if __name__ == "__main__":
    # Example usage of extract_sample_arrays
    arrays = TestAsciiConverter().extract_sample_arrays('data/training/aba27056.json')
    for i, array in enumerate(arrays):
        print(f"Array {i}:")
        for row in array:
            print(row)
    unittest.main()
