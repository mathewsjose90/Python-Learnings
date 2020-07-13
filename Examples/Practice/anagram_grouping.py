a = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

'''
res=[['ate','eat','tea'],
['nat','tan'],
['bat]]
'''

from itertools import groupby
from collections import Counter

res = []

for item in a:
    res.append((item, Counter(item)))
groups = []
for groupname, words in groupby(res, lambda x: sorted(x[1].items())):
    current_group = []
    for word in words:
        current_group.append(word[0])
    groups.append(current_group)
print(groups)
