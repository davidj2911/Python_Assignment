def merge_the_tools(s, k):
    n = len(s)
    for i in range(0, n, k):
        substring = s[i:i+k]
        new_substring = ''
        for char in substring:
            if char not in new_substring:
                new_substring += char
        print(new_substring)