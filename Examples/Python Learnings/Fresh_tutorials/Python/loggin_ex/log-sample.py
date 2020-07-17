import logging

logging.basicConfig(filename='testing.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    """Add function"""
    return x + y


def sub(x, y):
    """Subtract function"""
    return x - y


def mul(x, y):
    """Multiply function"""
    return x * y


def div(x, y):
    """Division function"""
    return x / y


num_1 = 100
num_2 = 25

add_res = add(num_1, num_2)
logging.debug(f"Add {num_1} + {num_2} = {add_res}")
sub_res = sub(num_1, num_2)
logging.debug(f"Sub {num_1} - {num_2} = {sub_res}")
mul_res = mul(num_1, num_2)
logging.debug(f"Mul {num_1} * {num_2} = {mul_res}")
div_res = div(num_1, num_2)
logging.debug(f"Div {num_1} / {num_2} = {div_res}")
