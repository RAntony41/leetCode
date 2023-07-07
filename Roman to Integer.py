class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = list(map(int,map(ord,s)))
        sum = 0
        
        
        for i in range(len(Roman)):
            if Roman[i] == 73:
                Roman[i] = 1
            if Roman[i] == 86:
                Roman[i] = 5
            if Roman[i] == 88:
                Roman[i] = 10
            if Roman[i] == 76:
                Roman[i] = 50
            if Roman[i] == 67:
                Roman[i] = 100
            if Roman[i] == 68:
                Roman[i] = 500
            if Roman[i] == 77:
                Roman[i] = 1000

        for i in range(len(Roman) - 1):
            if Roman[i] < Roman[i + 1]:
                sum -= Roman[i]
            if Roman[i] > Roman[i + 1] or Roman[i] == Roman[i + 1]:
                sum += Roman[i]
        
        sum += Roman[len(Roman) - 1]
        return sum
        



sol = Solution.romanToInt(0,"MDCLXVI")
print(sol)