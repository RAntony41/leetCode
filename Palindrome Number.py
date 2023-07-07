class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        Snum = list(str(x))
        ReSnum = list(str(x))
        ReSnum.reverse()
        n = len(Snum)

        #compare
        for i in range(n):
            A = int(Snum[i])
            B = int(ReSnum[i])
            if A != B :
                return False
                break
            
        return True


sol = Solution.isPalindrome(0,1000021)
print(sol)