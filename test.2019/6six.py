def complement(a, b):
    """
    deletes all elements(no duplicates) that are in b but not in a.
    """
    res = []
    for i in range(len(a)):
        n = True
        for j in range(len(b)):
            if a[i] == b[j]:
                n = False
                break
        if n:
            res.append(a[i])
    return res


print(complement(['python', 'a', 3, 'is', '3',
                  44, 'awesome'], ['3', 2, 1, 44, 3, 'a']))
