def solution(A):
    if len(A) == 1:
        return 0
    
    leader = find_leader(A)
    if leader is None:
        return 0
    
    left = left_leaders(A, leader)
    right = right_leaders(A, leader)
    count = 0
    breakpoint()
    for l, r in zip(left, right):
        if l and r:
            count += 1
    return count


def find_leader(A):
    size, top = 0, None
    for x in A:
        if size == 0:
            top = x
            size += 1
        else:
            if x == top:
                size += 1
            else:
                size -= 1
    count, n = 0, len(A)
    candidate = top
    for x in A:
        if x == candidate:
            count += 1
            if count > (n // 2):
                return candidate
    return None


def left_leaders(A, leader):
    curr, same = 0, []
    A = A[:-1]
    for length, x in enumerate(A, 1):
        if x == leader:
            curr += 1
        same.append(curr > (length // 2))
    return same


def right_leaders(A, leader):
    curr, same = 0, []
    A = A[1:]
    for length, x in enumerate(list(reversed(A)), 1): 
        if x == leader:
            curr += 1
        same.append(curr > (length // 2))
    same.reverse()
    return same


def test():
    assert solution([4, 3, 4, 4, 4, 2]) == 2


if __name__ == '__main__':
    test()

