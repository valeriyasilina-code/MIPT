#8 Defanging an IP Address (LeetCode 1108)
#https://leetcode.com/problems/defanging-an-ip-address/
def defangIPaddr(self, address: str) -> str:
        address=address.replace('.','[.]')
        return address



#9 Final Value of Variable After Performing Operations (LeetCode 2011)
#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

def finalValueAfterOperations(self, operations: list[str]) -> int:
        x=operations.count('++X')+operations.count('X++')-operations.count('X--')-operations.count('--X')
        return x


#10 Maximum Number of Words Found in Sentences (LeetCode 2114)
#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/


def mostWordsFound(self, sentences: list[str]) -> int:
        a=[i.count(' ')+1 for i in sentences]
        return max(a)
        



#11 Jewels and Stones (LeetCode 771)
#https://leetcode.com/problems/jewels-and-stones/description/


def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a=[i for i in stones if i in jewels]
        return len(a)


#12 Truncate Sentence (LeetCode 1816)
#https://leetcode.com/problems/truncate-sentence/description/

def truncateSentence(self, s: str, k: int) -> str:
        s=s.split()[0:k]
        return ' '.join(s)



#13 Reverse String (LeetCode 344)
#https://leetcode.com/problems/reverse-string/

def reverseString(self, s: list[str]) -> None:
        for i in range(len(s)//2):
            s[i],s[-(i+1)]=s[-(i+1)],s[i]
        return s



#14 Percentage of Letter in String (LeetCode 2278)
#https://leetcode.com/problems/percentage-of-letter-in-string/description/

def percentageLetter(self, s: str, letter: str) -> int:
        return int(s.count(letter)/len(s)*100)




#15 Uncommon Words from Two Sentences (LeetCode 884)
#https://leetcode.com/problems/uncommon-words-from-two-sentences/description/


def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s1=s1.split()
        s2=s2.split()
        ans=[]
        for i in s1:
            if s1.count(i)==1 and s2.count(i)==0:
                ans.append(i)
        for i in s2:
            if s2.count(i)==1 and s1.count(i)==0:
                ans.append(i)
        return ans


#16 Find the Difference (LeetCode 389)
#https://leetcode.com/problems/find-the-difference/description/


def findTheDifference(self, s: str, t: str) -> str:
        s=s+t
        let=[i for i in s if s.count(i)==1]
        return let[0]


#17 Maximum Number of Words You Can Type (LeetCode 1935)
#https://leetcode.com/problems/maximum-number-of-words-you-can-type/


def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s=text.split()
        ans=[]
        for word in s:
            a=[i for i in word if i in brokenLetters]
            if len(a)==0:
                ans.append(word)
        return len(ans)


#18 Repeated DNA Sequences (LeetCode 187)
#https://leetcode.com/problems/repeated-dna-sequences/description/


import re
def findRepeatedDnaSequences(self, s: str) -> list[str]:
        ans=[]
        for i in range(len(s)-9):
            s1=s[i:i+10]
            ma = re.findall(f'(?=({s1}))', s)
            if len(ma)>1 and s1 not in ans:
                ans.append(s1)
        return ans
