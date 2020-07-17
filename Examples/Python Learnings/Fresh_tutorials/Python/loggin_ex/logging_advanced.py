"""
Loggers , Handlers and Formatters
"""
import logging
import employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('testing.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s'))

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# logging.basicConfig(filename='testing.log', level=logging.DEBUG, format='%(asctime)s:%(name)s:%(message)s')


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
    try:
        res = x / y
    except ZeroDivisionError:
        logger.exception("Tried division by Zero")
    else:
        return x / y


num_1 = 100
num_2 = 0

add_res = add(num_1, num_2)
logger.debug(f"Add {num_1} + {num_2} = {add_res}")
sub_res = sub(num_1, num_2)
logger.debug(f"Sub {num_1} - {num_2} = {sub_res}")
mul_res = mul(num_1, num_2)
logger.debug(f"Mul {num_1} * {num_2} = {mul_res}")
div_res = div(num_1, num_2)
logger.debug(f"Div {num_1} / {num_2} = {div_res}")
