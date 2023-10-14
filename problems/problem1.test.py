import unittest
import problem1


class TestTask1(unittest.TestCase):
    def test_no_emotions(self):
        data = 'no emoji exists here'
        result = 0
        self.assertEqual(result, problem1.solve(data))

    def test_breaked_emotions(self):
        data = 'Good ;< ) morning ; <) ;< no :<0  valid)'
        result = 0
        self.assertEqual(result, problem1.solve(data))

    def test_one_emotion(self):
        data = '=-{)'
        result = 1
        self.assertEqual(result, problem1.solve(data))

    def test_many_emotions(self):
        data = '=-{)=-{)=-{)=-{)=-{)'
        result = 5
        self.assertEqual(result, problem1.solve(data))

    def test_emotions_with_splits(self):
        data = '[]=-{) hi ;;=-{)))      =-{)=-{)=-{)-<)'
        result = 5
        self.assertEqual(result, problem1.solve(data))


if __name__ == '__main__':
    unittest.main()
