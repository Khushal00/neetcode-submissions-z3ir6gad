class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for a, num in enumerate(nums):
            if num > 0:
                break
            if a > 0 and num == nums[a-1]:
                continue
            l, r = a + 1, len(nums) - 1
            while l < r:
                threeSum = nums[a] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1

        return res