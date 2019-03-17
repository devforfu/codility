# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    if len(H) == 1:
        return 1
    
    stack = [H.pop(0)]
    count = 0
    index = 0
    while index < len(H):
        x = H[index]
        if x > stack[-1]:
            index += 1
            stack.append(x)
        elif x == stack[-1]:
            index += 1
            continue
        else:
            count += 1
            stack.pop(-1)
            if not stack:
                index += 1
                stack = [x]
                
    return count + len(stack)

