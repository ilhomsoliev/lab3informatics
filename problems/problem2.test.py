import unittest
import problem2


class TestTask2(unittest.TestCase):

    def test_no_difference(self):
        data = 'nothing to change'
        result = 'nothing to change'
        self.assertEqual(result, problem2.solve(data))

    def test_one_short_form_time(self):
        data = 'I need to go at 10:00'
        respone = "I need to go at (TBD)"
        self.assertEqual(respone, problem2.solve(data))

    def test_one_long_form_time(self):
        data = 'I need to go at 10:21:40'
        respone = "I need to go at (TBD)"
        self.assertEqual(respone, problem2.solve(data))

    def test_2_at_the_same_time(self):
        data = 'We have party at 00:00 or you can say 12:00:00 AM'
        result = 'We have party at (TBD) or you can say (TBD) AM'
        self.assertEqual(result, problem2.solve(data))

    def test_out_of_bound(self):
        data = 'We will be there at 24:61'
        response = 'We will be there at 24:61'
        self.assertEqual(response, problem2.solve(data))

    def test_example(self):
        data = 'Уважаемые студенты! В эту субботу в 15:00 планируется доп. занятие на 2 часа. То есть в 17:00:01 оно уже точно кончится.'
        result = 'Уважаемые студенты! В эту субботу в (TBD) планируется доп. занятие на 2 часа. То есть в (TBD) оно уже точно кончится.'
        self.assertEqual(result, problem2.solve(data))

if __name__ == '__main__':
    unittest.main()
