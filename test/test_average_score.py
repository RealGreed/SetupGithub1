import unittest
from main_source import average_score

class MyTestCase(unittest.TestCase):
    def test_average_one_one(self):
        self.assertEqual(1, average_score.average(1,1))


if __name__ == '__main__':
    unittest.main()
