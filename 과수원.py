#첫째줄에 거래일수 N
#둘째줄에  매일 생산되는 과일  정수배열 P의 원소 N개 sep=' '
#셋째 줄에 도매상의 주문 C의 원소 N개 sep=' '
#출력 = 하루 평균 매출 소수점 이하 3자리에서 반올림하여 2자리까지 출력

# days = int(input())
# products = list(map(int, input().split()))
# orders = list(map(int, input().split()))
days = 5
products = [2,3,3,2,1]
orders = [1,4,4,1,1]
stock, day = 0, 0
price = 100
earn = 0
for order, product in zip(orders, products):
    stock += product
    if stock >= order:
        totalPrice = price*order
        stock, order = (stock-order), 0
        earn += totalPrice
        price = 100
    else:
        price -= 20
    if price == 0:
        break
    day+=1

print(f"{earn/day:.2f}")

