def getDist(tuple1, tuple2):
    return (abs(tuple1[0] - tuple2[0])+abs(tuple1[1]-tuple2[1]))/2

def solution(numbers, hand):
    answer=[]
    numberPad = {1:(0,0),2:(0,1),3:(0,2),
                 4:(1,0),5:(1,1),6:(1,2),
                 7:(2,0),8:(2,1),9:(2,2),
                 '*':(3,0),0:(3,1),'#':(3,2)}
    hand = hand[0].upper()
    leftHand = (3, 0)
    rightHand = (3, 2)
    for num in numbers:
        if num in [1,4,7]:
            answer.append("L")
            leftHand = numberPad[num]
        elif num in [3,6,9]:
            answer.append("R")
            rightHand = numberPad[num]
        else:
            if getDist(leftHand,numberPad[num]) == getDist(rightHand,numberPad[num]):
                answer.append(hand)
                if hand =='L':
                    leftHand = numberPad[num]
                else:
                    rightHand = numberPad[num]
            elif getDist(leftHand,numberPad[num]) < getDist(rightHand,numberPad[num]):
                answer.append("L")
                leftHand = numberPad[num]
            else:
                answer.append("R")
                rightHand = numberPad[num]
    return ''.join(answer)



if __name__ == "__main__":
    numbers = [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
    hand = ['right','left','right']
    for s, n in enumerate(numbers):
        print(solution(n, hand[s]))