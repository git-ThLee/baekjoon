def solution(price, money, count):
    answer =  sum([price*i for i in range(1,count+1)]) - money if sum([price*i for i in range(1,count+1)]) - money > 0 else 0
    return answer