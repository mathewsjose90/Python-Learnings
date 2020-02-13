def longestPalindrome(s):
    start_pos = 0
    end_pos = 0
    result_arr = [[0] * len(s) for _ in range(len(s))]
    # initialze the diagonal elements with 1 . It means all substrings of length 1 is a palindrome anyway
    for i in range(len(s)):
        result_arr[i][i] = 1
    # Now initialize the substrings with length 2 . They are palindrom if both the characters are same
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            result_arr[i][i + 1] = 1
            start_pos, end_pos = i, i + 1
    # result_arr[i][j]==1 means the substring from i to j is a palindrome
    # Now check with all strings with length 3 and more if they are a palindrome
    # For them to be a palindrome the below condition should match
    # result_arr[i][j] is palindrome if s[i]==s[j] and result_arr[i+1][j-1] is a palindrome

    substring_len = 2
    while substring_len < len(s):
        for i in range(len(s)):
            j = i + substring_len
            # print("checking from ", i, j)
            if j < len(s):
                if s[i] == s[j] and result_arr[i + 1][j - 1] == 1:
                    result_arr[i][j] = 1
                    if (j - i) > (end_pos - start_pos):
                        start_pos, end_pos = i, j
                else:
                    result_arr[i][j] = 0
            else:
                break

        substring_len += 1
    return s[start_pos:end_pos + 1]


print(longestPalindrome("cbbd"))
