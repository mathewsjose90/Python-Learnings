student = {'name': 'Mathews', 'Age': 25, 'Place': 'India'}
print(student['name'])
print(student.get('Loc', 'EU'))
student['Loc'] = 'KN'
print(student)

new_details = {'Subjects': ['Comp', 'Math', 'Data'], 'Deg': 'Eng'}
student.update(new_details)
print(student)

del student['Loc']

deg=student.pop('Deg')
print(deg)