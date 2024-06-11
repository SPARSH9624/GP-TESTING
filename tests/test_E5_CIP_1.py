import unittest
import E5_CIP_1

class TestGraphs(unittest.TestCase):
    def test_read_file(self):
        expected_output ="[[], [[314, 215, 0], [643, 202, 1], [359, 152, 2], [579, 149, 3], [426, 120, 4], [500, 116, 5], [349, 270, 6], [616, 268, 7], [419, 308, 8], [527, 304, 9], [428, 215, 10], [501, 207, 11], [563, 82, 12], [680, 240, 13], [454, 360, 14], [263, 297, 15], [336, 74, 16]], [[4, 5], [5, 3], [3, 1], [1, 7], [7, 9], [9, 8], [8, 6], [6, 0], [0, 2], [2, 4], [2, 16], [16, 4], [5, 12], [12, 3], [1, 13], [13, 7], [9, 14], [14, 8], [6, 15], [15, 0], [10, 11], [10, 5], [10, 4], [10, 2], [10, 0], [10, 6], [10, 8], [10, 9], [9, 11], [11, 5], [11, 3], [11, 7], [11, 1]], []]"
        actual_output=E5_CIP_1.read_file("5 CIP_1.txt")
        self.assertEqual(actual_output,expected_output)

if __name__ == '__main__':
    unittest.main()