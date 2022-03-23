# 학생N 명의 국영수 점수가 주어졌을때 아래와 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성해보자
# 1. 국어 점수가 감소하는 순
# 2. 국어점수가 같으면 영어 점수가 증가하는 순
# 3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서
# 4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서 (아스키코드 기준)
import sys
### input ###
N = 12
# Junkyu 50 60 100
# SangKeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90

students = [sys.stdin.readline().split() for _ in range(N)]
students = {x[0]:list(map(int,x[1:])) for x in students}

students = dict(sorted(students.items(), key=lambda x: (-int(x[1][0]),(int(x[1][1])),(-int(x[1][2])),(x[0]) )))
print(students.keys())
