import unittest
from math_quiz.math_quiz import randomNumberLimit, randomOperator, calculateFunc


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomNumberLimit(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_randomOperator(self):
        valid_operators = set(['+', '-', '*', '/'])
        operator = randomOperator()
        self.assertIn(operator, valid_operators)

    def test_calculateFunc(self):
        
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            # Add more test cases
            (10, 3, '*', '10 * 3', 30),
            (8, 4, '-', '8 - 4', 4),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculateFunc(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
