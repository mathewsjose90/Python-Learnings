import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Class Setup")

    @classmethod
    def tearDownClass(cls):
        print("Class tearDown")

    def setUp(self):
        self.emp_1 = Employee('Mathews', 'Jose', 3000)
        self.emp_2 = Employee('John', 'Roy', 5000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Mathews.Jose@test.com')
        self.assertEqual(self.emp_2.email, 'John.Roy@test.com')

        self.emp_1.first = 'Nick'
        self.emp_2.first = 'Sec'

        self.assertEqual(self.emp_1.email, 'Nick.Jose@test.com')
        self.assertEqual(self.emp_2.email, 'Sec.Roy@test.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Mathews Jose')

        self.emp_2.first = 'Nick'
        self.assertEqual(self.emp_2.fullname, 'Nick Roy')

    def test_apply_raise(self):
        self.assertEqual(self.emp_1.pay, 3000)
        self.assertEqual(self.emp_2.pay, 5000)

        self.emp_1.apply_raise()

        self.assertEqual(self.emp_1.pay, 3300)
        self.assertEqual(self.emp_2.pay, 5000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('July')
            mocked_get.assert_called_with('http://company.com/Jose/July')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Roy/June')
            self.assertEqual(schedule, 'Bad response!!!')


if __name__ == '__main__':
    unittest.main()
