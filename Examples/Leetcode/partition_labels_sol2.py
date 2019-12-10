'''
https://leetcode.com/problems/partition-labels/
'''


class Solution:
    def partitionLabels(self, S):
        char_last_seen, result, max_pos = {}, [], 0
        for i, c in enumerate(S):
            char_last_seen[c] = i
        count = 0
        for i, c in enumerate(S):
            max_pos = max(max_pos, char_last_seen[c])
            count += 1
            if i == max_pos:
                result.append(count)
                count = 0
        return result


def main():
    S = Solution()
    print(S.partitionLabels("ababcbacadefegdehijhklij"))
    print(S.partitionLabels("yyzababczbacadefegdkdkfkdkfkdkfehijhklij"))


if __name__ == '__main__':
    main()
