def solution(A):
    if not A:
        return 0
    if len(A) == 1:
        return 0
    deltas = [y - x for x, y in zip(A[:-1], A[1:])]
    return max_profit(deltas)


def max_profit(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


def test():
    assert solution([23171, 21011, 21123, 21013, 21367]) == 356
    assert solution([120, 250, 356, 280, 170, 400, 500]) == 380
    assert solution([100, 105, 110, 150, 200, 100, 300]) == 200 


if __name__ == '__main__':
    test()

