def word_order(n, words):
    count = {}
    for x in words:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1

    unique = list(count.keys())
    repeat = list(count.values())

    return len(unique), repeat