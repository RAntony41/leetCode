'''
class Solution:
    def maxArea(self, height: int) -> int:
        max = 0
        temp = 0
        num = len(height)
        for i in range(len(height)):

            for j in range(len(height)):
                if height[i] <= height[j]:
                    temp = height[i] * abs(j - i)
                
                if temp > max:
                    max = temp

        return max

sol = Solution.maxArea(0,[1,6,3])
print(sol)
'''

class Solution:
    def maxArea(self, height: int) -> int:
        left = 0
        right = len(height) - 1
        Amax = 0
        temp = 0

        while left < right:
            temp = (right - left) * min(height[left],height[right])
            Amax = max(temp, Amax)

            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1

        return Amax



sol = Solution.maxArea(0,[1,9,3])
print(sol)