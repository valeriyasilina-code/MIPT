#29 Design Parking System (LeetCode 1603)
#https://leetcode.com/problems/design-parking-system/
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.medium=medium
        self.small=small

    def addCar(self, carType: int) -> bool:
        if carType==1 and self.big>0:
            self.big-=1
            return True
        elif carType==2 and self.medium>0:
            self.medium-=1
            return True
        elif carType==3 and self.small>0:
            self.small-=1
            return True
        return False


#30 Simple Bank System (LeetCode 2043)
#https://leetcode.com/problems/simple-bank-system/description/

class Bank:

    def __init__(self, balance: list[int]):
        self.balance=balance
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1-=1
        account2-=1
        if 0<=account2<len(self.balance) and 0<=account1<len(self.balance) and self.balance[account1]>=money:
            self.balance[account1]-=money
            self.balance[account2]+=money
            return True
        return False

        

    def deposit(self, account: int, money: int) -> bool:
        account-=1
        if 0<=account<len(self.balance):
            self.balance[account]+=money
            return True
        return False
        

    def withdraw(self, account: int, money: int) -> bool:
        account-=1
        if 0<=account<len(self.balance) and self.balance[account]>=money:
            self.balance[account]-=money
            return True
        return False
