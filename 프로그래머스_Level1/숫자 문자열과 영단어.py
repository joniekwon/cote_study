def solution(s):
    numDict = {'one': '1', 'two': '2', 'three': '3', 'four': '4','five': '5',
                'six': '6', 'seven': '7', 'eight': '8', 'nine': '9','zero':'0'}

    for key, value in numDict.items():
        answer= s.replace(key, value)

    return answer

if __name__ == "__main__":
    inputStr = ["one4seveneight", "23four5six7", "2three45sixseven", "123"]
    for str in inputStr:
        print(solution(str))