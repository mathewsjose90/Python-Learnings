'''
https://leetcode.com/problems/longest-consecutive-sequence/
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''


def longestConsecutive(a):
    a_set = set(a)
    longest_length = 0
    for i in a:
        if i not in a_set:
            continue  # Item already counted. So it was removed from the set , in below code
        current_length = 1
        current_entry = i
        while i + 1 in a_set:  # Check all consecutive items to the right of current item
            current_length += 1
            i += 1
            a_set.remove(i)  # removing the entry , so that we wont be checking it again as it is already counted
        while current_entry - 1 in a_set:  # Check all consecutive items to the left of current item
            current_length += 1
            current_entry -= 1
            a_set.remove(
                current_entry)  # removing the entry , so that we wont be checking it again as it is already counted
        if current_length > longest_length:
            longest_length = current_length
    return longest_length


def longestConsecutive_approach1(a):
    a_set = set(a)
    longest_length = 0
    for i in a:
        current_length = 1
        current_entry = i
        while i + 1 in a_set:
            current_length += 1
            i += 1
        while current_entry - 1 in a_set:
            current_length += 1
            current_entry -= 1
        if current_length > longest_length:
            longest_length = current_length
    return longest_length


arr = [100, 4, 200, 1, 101, 3, 2, 5]
print(longestConsecutive(arr))
