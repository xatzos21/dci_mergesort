import unittest
from mergesort import mergesort


class TestMergeSort(unittest.TestCase):
    def test_duplicate(self):
        arr = [3, 2, 1, 2, 3]
        mergesort(arr)
        self.assertEqual(arr, [1, 2, 2, 3, 3])

    def test_sorted(self):
        arr = [1, 2, 3, 4, 5]
        mergesort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
