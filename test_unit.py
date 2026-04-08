import unittest
from logic import validate_probabilities, roll_dice

class Test(unittest.TestCase):

    def test_sum(self):
        try:
            validate_probabilities([0.1]*6)
            self.fail()
        except:
            pass

    def test_negative(self):
        try:
            validate_probabilities([0.5,-0.1,0.2,0.1,0.2,0.1])
            self.fail()
        except:
            pass

    def test_roll(self):
        r = roll_dice([1/6]*6, 50)
        for x in r:
            self.assertTrue(1 <= x <= 6)

if __name__ == "__main__":
    unittest.main()