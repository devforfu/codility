def slow_max_slice(A):
    n = len(A)
    result = 0
    for p in range(n):
        for q in range(p, n):
            total = 0
            for i in range(p, q + 1):
                total += A[i]
            result = max(result, total)
    return result


def quadratic_max_slice(A):
    n = len(A)
    result = 0
    pref = prefix_sum(A)
    for p in range(n):
        for q in range(p, n):
            total = pref[q + 1] - pref[p]
            result = max(result, total)
    return result


def prefix_sum(A):
    total = 0
    pref = [total]
    for x in A:
        total += x
        pref.append(total)
    return pref


def test():
    assert slow_max_slice([5, -7, 3, 5, -2, 4, -1]) == 10


if __name__ == '__main__':
    test()

