def select(a, way='incr'):
    """
    selection sort of the list a
    incr - increasing order
    decr - decreasing order
    """
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j] and way == 'incr':
                a[i], a[j] = a[j], a[i]
            elif a[i] < a[j] and way == 'decr':
                a[i], a[j] = a[j], a[i]
    return a


print(select([8, 1, 3, 2], 'decr'))
