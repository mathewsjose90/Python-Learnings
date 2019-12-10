import itertools

# count
print("count example")
counter = itertools.count(1)
print(next(counter))
print(next(counter))

lst = [10, 20, 30, 40]
list_pos = list(zip(counter, lst))
print(list_pos)

# zip_longest

data = [100, 200, 300, 400]
data_pos = list(itertools.zip_longest(range(10), data))
print(data_pos)

# cycle

data = [1, 2, 3]
counter = itertools.cycle(data)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

# repeat

squares = list(map(pow, range(10), itertools.repeat(2)))
print(squares)

counter = itertools.repeat(5, times=3)
for i in counter:
    print(i)

# starmap

squares = list(itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)]))
print(squares)

# permutations and combinations and product

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
names = ['Mathews', 'Jose']
print(list(itertools.permutations(letters, 2)))
print(list(itertools.combinations(letters, 2)))
print(list(itertools.product(numbers, repeat=2)))

# chain

combined = itertools.chain(letters, numbers, names)
for item in combined:
    print(item)

# islice
print("\nislice example")
result = itertools.islice(range(10, 20, 2), 1, 5)
for i in result:
    print(i)
with open('test.log') as f:
    header = itertools.islice(f, 3)
    for info in header:
        print(info, end='')

# compress
print("\ncompress example")
names = ['a', 'b', 'c', 'd']
selectors = [True, False, True, True]
print(list(itertools.compress(names, selectors)))  # return only entries that makes true for the selector

# filterfalse
print("\nfilterfalse example")


def lt_3(n):
    if n < 3:
        return True
    return False


d = [2, 4, 5, 1, 0]
print(list(itertools.filterfalse(lt_3, d)))

# dropwhile
print("\ndropwhile example")
d = [10, 20, 30, 40, 50, 25, 35, 100]
print(
    list(itertools.dropwhile(lambda x: x < 40, d)))  ##Drop the elements till the condition becomes false for first time

# takewhile
print("\ntakewhile example")
print(list(itertools.takewhile(lambda x: x < 40, d)))  ##opposite of the above dropwhile function

# accumulate
print("\naccumulate example")
data = [1, 3, 4, 5, 6]
result = itertools.accumulate(data, lambda x, y: x + y)  ##accumulate the values as it goes through the iterator
for d in result:
    print(d)  ##Similar to reduce . But reduce will return only 1 value after all accumulations

# groupby
print("\ngroupby example")


def get_dept(e):
    return e['dept']


employees = [{'name': 'Mathews', 'dept': 'Eng'},
             {'name': 'John', 'dept': 'Eng'},
             {'name': 'Ann', 'dept': 'Gov'},
             {'name': 'Mar', 'dept': 'IT'}]
dept_groups = itertools.groupby(employees, get_dept)  # groupby will only work if the key field is already sorted
for key, group in dept_groups:
    print(key)
    for emp in group:
        print(emp)
