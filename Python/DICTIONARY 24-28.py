#24 Majority Element (LeetCode 169)
#https://leetcode.com/problems/majority-element/

def majorityElement(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key,val in d.items():
            if val>len(nums)/2:
                return key

#25 Keyboard Row (LeetCode 500)
#https://leetcode.com/problems/keyboard-row/description/
def findWords(self, words: list[str]) -> list[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        ans=[]
        for w in words:
            w.lower()
            a1=[i for i in w if i in row1]
            a2=[i for i in w if i in row2]
            a3=[i for i in w if i in row3]
            if (len(a1)==0)+(len(a2)==0)+(len(a3)==0)==2:
                ans.append(w)
        return ans
              
              
#26 Sum of Unique Elements (LeetCode 1748)
#https://leetcode.com/problems/sum-of-unique-elements/

def sumOfUnique(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=[key for key, val in d.items() if val==1]
        return sum(a)

  
#27 Rings and Rods (LeetCode 2103)
#https://leetcode.com/problems/rings-and-rods/description/

def countPoints(self, rings: str) -> int:
        d={}
        for i in range(0,len(rings)-1,2):
            if rings[i+1] in d:
                d[rings[i+1]].append(rings[i])
            else:
                d[rings[i+1]]=[rings[i]]
        c=0
        for key, value in d.items():
            if len(set(value))==3:
                c+=1
        return c

  
#28 Two Out of Three (LeetCode 2032)
#https://leetcode.com/problems/two-out-of-three/
def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        ans=[]
        for i in nums1+nums2+nums3:
            if i not in ans and (i in nums1)+(i in nums2)+(i in nums3)>=2:
                ans.append(i)
        return ans
