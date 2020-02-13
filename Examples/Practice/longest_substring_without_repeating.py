def longest_substring(s):
    longest_sub = ""
    current_sub = ""
    for c in s:
        if c not in current_sub:
            current_sub += c
        else:
            if len(current_sub) > len(longest_sub):
                longest_sub = current_sub
                i=current_sub.index(c)
                current_sub = current_sub[i+1:]+c

    return longest_sub if len(current_sub) < len(longest_sub) else current_sub


print(longest_substring('ABDEFGABEF'))
