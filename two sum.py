class Solution:
    def twoSum(self, nums: int, target: int):
        list = {}
        for i,n in enumerate(nums):
            diff = target - n

            if diff in list:
                return [list[diff],i]

            list[n] = i


sol = Solution.twoSum(0, [11,2,7,15], 9)
print(sol)