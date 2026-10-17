#1 Convert the Temperature (LeetCode 2469)
#https://leetcode.com/problems/convert-the-temperature/
def convertTemperature(self, celsius: float) -> list[float]:
      Kelvin = celsius + 273.15
      Fahrenheit = celsius * 1.80 + 32.00
      return [Kelvin, Fahrenheit]


#2 Robot Return to Origin (LeetCode 657)
#https://leetcode.com/problems/robot-return-to-origin/
def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for i in moves:
            if i=="L":x-=1
            elif i=="R": x+=1
            elif i=="U": y+=1
            else: y-=1
        if x==0 and y==0:
            return(True)
        else:
            return(False)


#3 Valid Palindrome (LeetCode 125)
#https://leetcode.com/problems/valid-palindrome/
def isPalindrome(self, s: str) -> bool:
        s_new = "".join(c for c in s if c.isalnum())
        s_new=s_new.lower()
        for i in range(len(s_new)//2):
            if s_new[i]!=s_new[-(i+1)]:
                return False
        return True



#4 Valid Anagram (LeetCode 242)
#https://leetcode.com/problems/valid-anagram/

def isAnagram(self, s: str, t: str) -> bool:
        a=[[s.count(i), i] for i in s]
        b=[[t.count(i), i] for i in t]
        return sorted(a)==sorted(b)
        # или просто return sorted(s)==sorted(t)



#5 Pascal's Triangle (LeetCode 118)
#https://leetcode.com/problems/pascals-triangle/

def generate(self, numRows: int) -> list[list[int]]:
        s=[[1]]
        for i in range(1,numRows):
            s.append([1])
            for j in range(0,len(s[i-1])-1):
                s[i].append(s[i-1][j]+s[i-1][j+1])
            s[i].append(1)
        return s




#6 Can Place Flowers (LeetCode 605)
#https://leetcode.com/problems/can-place-flowers/


def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        c=0
        for i in range(len(flowerbed)):
            if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                c+=1
            elif i==len(flowerbed)-1 and flowerbed[i]==0 and flowerbed[i-1]==0:
                c+=1
            elif flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                c+=1
        return c>=n







#7 Find Winner on a Tic Tac Toe Game (LeetCode 1275)
#https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/


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
        
