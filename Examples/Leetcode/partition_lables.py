'''
https://leetcode.com/problems/partition-labels/
'''


class Solution:
    def partitionLabels(self, S):
        l = len(S)
        i = 0
        parts = []
        while i < l:
            for j in range(l - 1, i - 1, -1):
                if S[i] == S[j]:
                    remaining_part = S[j:]
                    repeating_pos = j
                    chars_to_check = list(set(S[i:j + 1]))
                    for c in chars_to_check:
                        # print('Checking '+c+' in '+remaining_part)
                        if c in remaining_part:
                            repeating_pos = max(repeating_pos, j + remaining_part.rindex(c))
                            chars_to_check.extend([c for c in S[j + 1:repeating_pos + 1] if c not in chars_to_check])
                    # print("appending : "+S[i:repeating_pos+1])
                    parts.append(S[i:repeating_pos + 1])
                    i = repeating_pos + 1
                    break
                if i == j:
                    parts.append(S[i:j + 1])
                    i += 1
                    break
        # print(parts)
        return [len(s) for s in parts]


def main():
    S = Solution()
    print(S.partitionLabels("ababcbacadefegdehijhklij"))


if __name__ == '__main__':
    main()
