class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        flag=True
        i=1
        while flag:
            a=strs[0][:i]
            for word in strs[1:]:
                if not(len(word)>=len(a) and word[:i]==a):
                    flag=False
                    break
            if flag: i+=1
        return strs[0][:i-1]

        
