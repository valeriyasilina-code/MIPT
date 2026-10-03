#Трибоначчи
def tribonacci(self, n: int) -> int:
        if n==0: return 0
        elif n in [1,2]: return 1
        else: return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)
tribonacci(25)



#TwoSum

from typing import List


def twoSum(self, nums: list[int], target: int) -> list[int]:
        ans=[]
        for i in range(len(nums)):
            if target - nums[i] in nums and i!=nums.index(target - nums[i]):
                ans.append( [i, nums.index(target - nums[i])])
                return ans[0]


#Крестики Нолики
def tictactoe(self, moves: list[list[int]]) -> str:
        first = moves[::2]
        second = moves[1::2]
        first_rows=[a[0] for a in first]
        first_col=[a[1] for a in first]
        second_rows=[a[0] for a in second]
        second_col=[a[1] for a in second]
        first_d1=[1 for a in first if a[0]==a[1]]
        first_d2=[1 for a in first if a[0]+a[1]==2]
        second_d1=[1 for a in second if a[0]==a[1]]
        second_d2=[1 for a in second if a[0]+a[1]==2]
        if len(first)>=3 and (len(first_d1)==3 or len(first_d2)==3 or any(first_rows.count(x)==3 for x in first_rows) or any(first_col.count(x)==3 for x in first_col)):
            return "A"
        elif len(second) >=3 and (len(second_d1)==3 or len(second_d2)==3 or any(second_rows.count(x)==3 for x in second_rows) or any(second_col.count(x)==3 for x in second_col)):
          return "B"
        elif len(moves)==9:
          return  "Draw"
        else:
          return "Pending"
        



