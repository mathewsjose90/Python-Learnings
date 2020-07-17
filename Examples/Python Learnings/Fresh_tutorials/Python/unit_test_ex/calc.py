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
    if y == 0:
        raise ValueError('Tried division by 0')
    return x / y
