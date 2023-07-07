class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = ''.join(s).split()
        count = len(length)
        word = length[count - 1]
        return len(word)
        

sol = Solution.lengthOfLastWord(0,"Hello World")
print(sol)