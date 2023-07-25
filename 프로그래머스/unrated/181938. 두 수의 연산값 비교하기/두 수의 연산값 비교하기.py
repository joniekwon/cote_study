def solution(a, b):
    f1 = int(str(a) + str(b))
    f2 = 2 * a * b
    
    return f1 if f1 >= f2 else f2