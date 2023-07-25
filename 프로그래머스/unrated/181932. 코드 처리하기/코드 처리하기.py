def solution(code):
    ret = ''
    mode = False
    for idx in range(len(code)):
        if code[idx] == "1":
            mode = not mode
            continue
        if idx % 2 == mode:
            ret += code[idx]
        
    return ret if bool(ret) else "EMPTY"