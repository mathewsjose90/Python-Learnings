import requests


class Employee:
    raise_amount = 1.10

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@test.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.email}')"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return "Bad response!!!"
