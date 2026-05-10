def solution(price, money, count):
    total = 0
    for i in range(count):
        total += price + price * i 

    if total > money: 
        return total - money
    return 0