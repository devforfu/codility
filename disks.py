def solution_slow(a):
    cuts = [(c - r, c + r) for c, r in enumerate(a)]
    cuts.sort(key=lambda pair: pair[0])
    n = len(cuts)
    total = 0
    for i in range(n):
        l1, r1 = cuts[i]
        for j in range(i+1, n):
            l2, _ = cuts[j]
            if l1 <= l2 <= r1:
                total += 1
            if total > 10e7:
                return -1
    return total

def solution_copy(a):
    import bisect
    cuts = [(c - r, c + r) for c, r in enumerate(a)]
    cuts.sort(key=lambda pair: pair[0])
    lefts, rights = zip(*cuts)
    n = len(cuts)
    total = 0
    for i in range(n):
        r = rights[i]
        pos = bisect.bisect_right(lefts[i+1:], r)
        total += pos
        if total > 10e7:
            return -1
    return total

def solution(a):
    import bisect
    if len(a) <= 1:
        return 0
    cuts = [(c - r, c + r) for c, r in enumerate(a)]
    cuts.sort(key=lambda pair: pair[0])
    lefts, rights = zip(*cuts)
    n = len(cuts)
    total = 0
    for i in range(n):
        r = rights[i]
        pos = bisect.bisect_right(lefts, r)
        total += (pos - i - 1)
        if total > 10e6:
            return -1
    return total

def test():
    assert solution([1, 5, 2, 1, 4, 0]) == 11

if __name__ == '__main__':
    test()

