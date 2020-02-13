def reverse_string(s, start, end):
    while start < end:
        '''
        Using XOR to swap 2 variable
        a=a^b
        b=a^b
        a=a^b
        '''

        s = s[:start] + chr(ord(s[start]) ^ ord(s[end])) + s[start + 1:]
        s = s[:end] + chr(ord(s[start]) ^ ord(s[end])) + s[end+1:]
        s = s[:start] + chr(ord(s[start]) ^ ord(s[end])) + s[start + 1:]
        start += 1
        end -= 1
    return s


s = "Testing"
print(reverse_string(s, 0, len(s) - 1))
