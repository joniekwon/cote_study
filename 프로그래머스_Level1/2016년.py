import datetime

def solution(a,b):
    date = datetime.datetime(2016,a,b)
    weekdays = {0:'MON',1:'TUE',2:'WED',3:'THU',4:'FRI',5:'SAT',6:'SUN'}
    return weekdays[date.weekday()]



if __name__ == "__main__":
    a,b = 5, 24
    print(solution(a,b))