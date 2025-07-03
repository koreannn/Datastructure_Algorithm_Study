class Coin():
    def __init__(self, unit):
        self.unit = unit # 거스름돈 단위
        self.count = 0

def ChageCoin(money: int):
    print(f"{money}원 거슬러주기")
    coins = []
    
    coins.append(Coin(500))
    coins.append(Coin(100))
    coins.append(Coin(50))
    coins.append(Coin(10))
    
    for i in range(len(coins)):
        while coins[i].unit <= money:
            coins[i].count += 1
            money -= coins[i].unit
            
    for i in range(len(coins)):
        print(f"{coins[i].unit}원 {coins[i].count}개")

ChageCoin(2300)
    