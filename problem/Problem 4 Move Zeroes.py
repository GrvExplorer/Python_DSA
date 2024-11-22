

class Solution(object):
    def moveZeroes(self, nums: list):
      for x in range(0, len(nums)):
       try:
        nums.index(0) 
        if True:
          nums.remove(0)
          nums.append(0)
          continue
       except:
         break
      return

zeroes = Solution()

ran_zeros = [0]
zeroes.moveZeroes(ran_zeros)
print(ran_zeros)
        