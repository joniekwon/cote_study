import re
def solution(inputID):
    # 1단계: 소문자 바꾸기
    new_id = inputID.lower()
    #2단계 - . _ 제외한 문자열 제거
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)

    #3단계 : 2번 이상 연속된 ..을 .으로 치환
    while new_id.find('..') >= 0:  #.find() 찾은 문자열의 인덱스를 반환
        new_id = new_id.replace('..', '.')
    #4단계 : 처음과 끝의 . 제거
    new_id = new_id.strip('.')
    #5단계 : 빈 문자열일 경우  a 대입
    if new_id == '':
        new_id = 'a'
    #6단계 16자 이상이면 15개를 제외한 나머지 삭제, 끝이 .으로 끝날경우 . 삭제
    if len(new_id)>15:
        new_id = new_id[:15]
    new_id = new_id.rstrip('.')
    #7단계
    while len(new_id)<3:
        new_id = new_id + new_id[-1]
    return new_id

if __name__ == '__main__':
    inputs = ['...!@BaT#*..y.abcdefghijklm',"z-+.^.","=.=","123_.def","abcdefghijklmn.p"]
    for inputID in inputs:
        print(solution(inputID))