import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        logger.info(f'Create Employee: {self.fullname} - {self.email}')

    @property
    def email(self):
        return f"{self.first}.{self.last}@test.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.email}')"


emp_1 = Employee('mathews', 'Jose', 10000)
emp_2 = Employee('Nick', 'John', 50000)
