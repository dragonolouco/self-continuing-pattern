import unittest

from src.fundamental_engine import add_with_trace, subtract_with_trace


class FundamentalEngineTests(unittest.TestCase):
    def test_addition_example(self):
        result, steps = add_with_trace(5897, 7648)
        self.assertEqual(result, 13545)
        self.assertEqual(len(steps), 4)
        self.assertEqual(steps[-1].state_out, 1)

    def test_addition_without_carry(self):
        result, steps = add_with_trace(11, 22)
        self.assertEqual(result, 33)
        self.assertTrue(all(step.state_out == 0 for step in steps))

    def test_addition_reuses_same_rule_for_long_inputs(self):
        left = int("9" * 100)
        right = 1
        result, steps = add_with_trace(left, right)
        self.assertEqual(result, int("1" + "0" * 100))
        self.assertEqual(len(steps), 100)
        self.assertEqual(steps[0].state_out, 1)

    def test_subtraction_with_borrow(self):
        result, steps = subtract_with_trace(532, 178)
        self.assertEqual(result, 354)
        self.assertTrue(any(step.state_out == 1 for step in steps))

    def test_invalid_subtraction_is_rejected(self):
        with self.assertRaises(ValueError):
            subtract_with_trace(1, 2)


if __name__ == "__main__":
    unittest.main()
