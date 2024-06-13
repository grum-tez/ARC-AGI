import unittest
from altfunctions import convert_grid, convert_back_grid, add_horizontal_borders, remove_horizontal_borders
from test_asciiconverter import TestAsciiConverter

class TestAltFunctions(unittest.TestCase):\

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
    
    def test_basic_matrix_conversion(self):
        print("tesing basic matrix conversion")
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

    def test_add_and_remove_horizontal_borders(self):
        ascii_art = "|*|#|@|\n--|-|--\n|%|&|O|\n--|-|--\n|$|X|~|"
        bordered_art = add_horizontal_borders(ascii_art)
        print("ASCII ART WITH BORDERS:")
        print(bordered_art)
        self.assertTrue(bordered_art.startswith("_"))
        self.assertTrue(bordered_art.endswith("‾"))

        restored_art = remove_horizontal_borders(bordered_art)
        print("RESTORED ASCII ART WITHOUT BORDERS:")
        print(restored_art)
        self.assertEqual(restored_art, ascii_art)

    def check_matrix_array(self, arrays):
        summary = {"True": 0, "False": 0}
        for array in arrays:
            if self.check_matrix(array):
                summary["True"] += 1
            else:
                summary["False"] += 1
        assert summary["False"] == 0, f"Found {summary['False']} matrices that failed conversion."
        return summary

    def test_all_json_files_in_training_folder(self):
        import os

        training_folder = 'data/training'
        json_files = [f for f in os.listdir(training_folder) if f.endswith('.json')]

        false_zero_count = 0
        false_greater_than_zero_count = 0

        for json_file in json_files[:400]:
            json_file_path = os.path.join(training_folder, json_file)
            arrays = TestAsciiConverter().extract_sample_arrays(json_file_path)
            summary = self.check_matrix_array(arrays)
            if summary["False"] == 0:
                false_zero_count += 1
            else:
                false_greater_than_zero_count += 1

        print(f"Number of JSON files: {len(json_files)}")
        print(f"Files with False: 0: {false_zero_count}")
        print(f"Files with False > 0: {false_greater_than_zero_count}")

if __name__ == "__main__":
    unittest.main()
