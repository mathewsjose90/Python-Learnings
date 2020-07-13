def mysingleton(cls):
    _instances = {}

    def wrapper(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return wrapper


@mysingleton
class MyClass:
    def __init__(self, name='Mathews'):
        self.name = name


m = MyClass('Mathews')
print(m.name)
n = MyClass('Nick')
print(n.name)
