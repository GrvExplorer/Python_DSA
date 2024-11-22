class Solution(object):
  def twoSum(self, nums, target):
    for f in range(len(nums)):
      for s in range(len(nums)):
        if f == s:
          continue
        that = nums[f] + nums[s]
        if that == target:
          return [f, s]
        continue
      
solution1 = Solution()

print(solution1.twoSum([3, 8, 9, 10], 19))
