'''
https://leetcode.com/problems/group-anagrams/
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
import itertools


class Solution:
    def groupAnagrams(self, strs):
        result = []
        groups = itertools.groupby((sorted(strs, key=sorted)), sorted)
        for group_key, value in groups:
            result.append(list(value))
        return str(result)


s = Solution()
print(s.groupAnagrams((["eat", "tea", "tan", "ate", "nat", "bat"])))
