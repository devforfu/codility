# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(a, b):
    if len(a) == 1:
        return 1
    
    n = len(b)
    total = sum(b)
    if total == n or total == 0:
        return n
        
    alive = 0
    for x in b:
        if x == 1:
            break
        alive += 1
    
    index = alive
    stack = [a[index]]
    index += 1
    
    while index < n:
        upstream = b[index] == 0
        downstream = not upstream
        if not stack and upstream:
            alive += 1
        elif downstream:
            stack.append(a[index])
        elif upstream:
            while stack:
                fish = stack[-1]
                curr = a[index]
                if fish > curr:
                    break
                stack.pop(-1)
            if not stack:
                alive += 1
        index += 1
        
    return len(stack) + alive
        
            
        
