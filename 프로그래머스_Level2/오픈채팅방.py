def solution(record):
    answer = []
    #0 : Enter, Leave, Change 중 하나
    #1 : user ID
    #2 : nickname
    logDict = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    nickNames = {}

    for rec in record:
        try:
            log, userID, nickName = rec.split()
            nickNames[userID] = nickName
        except: # Leave 일때만
            log, userID = rec.split()

        if log !='Change':
            answer.append(userID+ ' ' + log)

    for i, rec in enumerate(answer):
        userID, log = rec.split()
        answer[i] = nickNames[userID]+logDict[log]

    return answer

x = ["Prodo님이 들어왔습니다.","Ryan님이 들어왔습니다.","Prodo님이 나갔습니다","Prodo님이 들어왔습니다."]
y = ["Prodo님이 들어왔습니다.","Ryan님이 들어왔습니다.","Prodo님이 나갔습니다.","Prodo님이 들어왔습니다."]
if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))