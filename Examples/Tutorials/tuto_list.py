c = ['Maths', 'Eng', 'Computer']
c1 = ['Chem', 'Phy']
c2 = ['Data', 'Mech']
c.append(c1)
print(c)
c.extend(c2)
c.insert(0, 'Test')
print(c)
print(c.pop())
c.reverse()
c.remove(c1)
print(c)
c.sort()
print(c)
new_c = sorted(c, reverse=True)
print(new_c)

nums = [12, 44, 5, 4, 66, 7, 88, 90, 10]
print(min(nums))
print(max(nums))
print(sum(nums))
print(nums.index(44))
print(90 in nums)

#sets

s1={'Mathews','Jose','123'}
s2={'John','Mathews','44'}
print(s1)
print(s1.intersection(s2))
print(s1.union(s2))
