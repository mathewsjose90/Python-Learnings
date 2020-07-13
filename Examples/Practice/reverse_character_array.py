'''
Given a array of characters reverse it such that each word remains same .Words are separated by space.
Try to do it without any extra space.

Ex:
['H','i' ,' ','M','a','t','h','e','w','s',' ','H','e','l','l','o']
==>['H','e','l','l','o',' ','M','a','t','h','e','w','s',' ','H','i']
'''

arr = ['H', 'i', ' ', 'M', 'a', 't', 'h', 'e', 'w', 's', ' ', 'H', 'e', 'l', 'l', 'o']

# reverse the entire array first
low, high = 0, len(arr) - 1
space_pos = []
while low < high:
    arr[low], arr[high] = arr[high], arr[low]
    if arr[low] == " ":
        space_pos.append(low)
    if arr[high] == " ":
        space_pos.append(high)
    low += 1
    high -= 1

space_pos.append(len(arr))
space_pos.sort()

# Now reverse each words in the array
low, high, word_count = 0, 0, 0
while word_count < len(space_pos):
    high = space_pos[word_count] - 1
    while low < high:
        arr[high], arr[low] = arr[low], arr[high]
        low += 1
        high -= 1
    low = space_pos[word_count] + 1
    word_count += 1

print(arr)
