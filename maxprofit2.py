"""
This solution doesn't pass one of the performance tests.
"""
def solution(A):
    if len(A) <= 1:
        return 0
    deltas = [y - x for x, y in zip(A[:-1], A[1:])]
    return max(max_profit(deltas), 0)


def max_profit(A):
    value, _, _ = max_slice(A, 0, len(A)-1)
    return value


def max_slice(A, p, q):
    if p == q:
        return A[p], p, q
    
    m = (p + q)//2
    l_sum, l_start, l_end = max_slice(A, p, m)
    r_sum, r_start, r_end = max_slice(A, m+1, q)
    m_sum, m_start, m_end = max_crossing_slice(A, p, m, q)
    
    best = max(l_sum, r_sum, m_sum)
    if best == l_sum:
        return l_sum, l_start, l_end
    elif best == r_sum:
        return r_sum, r_start, r_end
    else:
        return m_sum, m_start, m_end


def max_crossing_slice(A, p, m, q):
    left_sum, left_index = float('-inf'), None
    curr = 0
    for i in range(m, p-1, -1):
        curr += A[i]
        if curr > left_sum:
            left_sum = curr
            left_index = i
    right_sum, right_index = float('-inf'), None
    curr = 0
    for j in range(m+1, q+1):
        curr += A[j]
        if curr > right_sum:
            right_sum = curr
            right_index = j
    return (left_sum + right_sum), left_index, right_index

if __name__ == '__main__':
    assert solution([23171, 21011, 21123, 21013, 21367]) == 356

