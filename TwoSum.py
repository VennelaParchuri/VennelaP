# LeetCode problem 1 Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        list1 = []
        for i,value in enumerate(self.nums):
            difference = self.target - nums[i]
            if difference in self.nums and self.nums.index(difference)!=i:
                list1 = [i,self.nums.index(difference)]
                break
        return list1