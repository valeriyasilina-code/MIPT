#1. https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        lst=[n for n in str(abs(x))]
        lst.reverse()
        if x<0 and int('-'+''.join(lst))>=-2**31:
            return int('-'+''.join(lst))
        elif x>=0 and int(''.join(lst))<=2**31-1:
            return int(''.join(lst))
        else:
            return 0


#2. https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                b=0-nums[i]-nums[j]
                if b in nums[j+1:] and sorted([nums[i], nums[j],b]) not in ans:
                    ans.append(sorted([nums[i], nums[j],b]))  
        return ans      


#3. https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        import string
        alph=string.ascii_lowercase
        a=[]
        for i in range(len(digits)):
            if 2<=int(digits[i])<=6:
                a.append(alph[(int(digits[i])-2)*3:(int(digits[i])-2)*3+3])
            elif int(digits[i])==7:
                a.append('pqrs')
            elif int(digits[i])==8:
                a.append('tuv')
            else:
                a.append('wxyz')
        combinations = list(itertools.product(*a))
        res = ["".join(s) for s in combinations]
        return res

#4. https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[[]]
        for i in nums:
            new=[]
            for lst in ans:
                new.append(lst+[i])
            ans.extend(new)
        return ans


#5 https://leetcode.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        sm=triangle[0][0]
        j=0
        for lst in triangle[1:]:
            sm+=min(lst[j], lst[j+1])
            j+=(lst[j+1]<lst[j])
        return sm
        
