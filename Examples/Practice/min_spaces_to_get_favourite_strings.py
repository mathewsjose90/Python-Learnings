'''
n=3141592653589793238462643383279
fav_list=[100,3,314,15926535897932384,279,62643383279,89]
ans is 3
    314 15926535897932384 62643383279
'''

import sys


def get_min_spaces(s, fav):
    sub_string = ""
    space_count = 0
    min_space = sys.maxsize
    if s in fav:
        return 0
    for i, c in enumerate(s):
        sub_string += c
        if sub_string in fav:
            remaining_min_spaces = get_min_spaces(s[i + 1:], fav)
            if remaining_min_spaces != -1:
                min_space = min(min_space, 1 + remaining_min_spaces)

    return min_space if min_space != sys.maxsize else -1


def get_min_space_dp(dp, pos, s, fav):
    '''

    :param dp: dp array to store the result if the substring starting at index pos can be solved
    :param pos: position in the string from which substrings has to be checked
    :param s: string
    :param fav: favourite numbers
    :return:
    '''
    if dp[pos] != -2:
        return dp[pos]
    if s[pos:] in fav:
        dp[pos] = 0
        return dp[pos]
    min_space = sys.maxsize
    sub_string = ""
    for i, c in enumerate(s[pos:]):
        sub_string += c
        if sub_string in fav:
            remaining_spaces_needed = get_min_space_dp(dp, i + pos+1 , s, fav)
            if remaining_spaces_needed != -1:
                min_space = min(min_space, 1 + remaining_spaces_needed)
    dp[pos] = min_space if min_space != sys.maxsize else -1
    return dp[pos]


def main():
    # print(get_min_spaces('3141592653589793238462643383279',['3', '314', '50', '41', '159265358979', '9323846', '323', '8462643383279', '279']))
    input_string = input("Enter the string : ")
    favourite_numbers = input("Enter the favourie numbers separated by spaces :").split()
    print(get_min_spaces(input_string, favourite_numbers))
    # DP way
    dp = [-2 for x in range(len(input_string))]
    print(get_min_space_dp(dp, 0, input_string, favourite_numbers))


if __name__ == "__main__":
    main()
