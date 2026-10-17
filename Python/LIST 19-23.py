#19 Find Numbers with Even Number of Digits (LeetCode 1295)
#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

def findNumbers(self, nums: list[int]) -> int:
        n=[i for i in nums if len(str(abs(i)))%2==0]
        return len(n)


#20 Number of Good Pairs (LeetCode 1512)
#https://leetcode.com/problems/number-of-good-pairs/description/


def numIdenticalPairs(self, nums: list[int]) -> int:
        c=0
        for i in range (len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    c+=1
        return c

  
#21 Count Good Triplets (LeetCode 1534)
#https://leetcode.com/problems/count-good-triplets/description/
def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count=0
        for i in range(len(arr)-2):
            for j in range(i+1, len(arr)-1):
                for k in range(j+1,len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count+=1
        return count



  
#22 Matrix Diagonal Sum (LeetCode 1572)
#https://leetcode.com/problems/matrix-diagonal-sum/
def diagonalSum(self, mat: list[list[int]]) -> int:
        s=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j or i == len(mat)-1-j:
                    s+=mat[i][j]
        return s


  
#23 Min Max Game (LeetCode 2293)
#https://leetcode.com/problems/min-max-game/description/

def minMaxGame(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        i=1
        while 2**i<len(nums):
            i+=1
        nums2=[nums]
        for j in range(1,i):
            b=[]
            for h in range(0,len(nums2[j-1])-2,2):
                b.append(min(nums2[j-1][h],nums2[j-1][h+1]))
            nums2.append(b)
            print(nums2)
        return nums2[-1][0]
