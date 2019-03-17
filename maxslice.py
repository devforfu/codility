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


def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


def prefix_sum(A):
    total = 0
    pref = [total]
    for x in A:
        total += x
        pref.append(total)
    return pref


def test():
    example = [5, -7, 3, 5, -2, 4, -1] 
    assert slow_max_slice(example) == 10
    assert golden_max_slice(example) == 10


if __name__ == '__main__':
    test()

