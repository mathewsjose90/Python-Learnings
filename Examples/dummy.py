input_str = "always be coding"
results = []
already_visited = set()


def longest_substring_without_repeating_char(s):
    print("called with " + s)
    if len(s) != 1 and s not in already_visited:
        already_visited.add(s)
        if len(s) == len(set(s)):
            print("Found")
            results.append(s)

        longest_substring_without_repeating_char(s[1:])
        longest_substring_without_repeating_char(s[:-1])



print(longest_substring_without_repeating_char(input_str))
print(max([(len(x), x) for x in results]))



