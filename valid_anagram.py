class Solution:
    def helper(self, s:str):
        myDict = {}
        for letter in s:
            if letter in myDict:
                myDict[letter] += 1
            else:
                myDict[letter] = 1
        return myDict
        
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = self.helper(s)
        s2 = self.helper(t)

        return s1 == s2