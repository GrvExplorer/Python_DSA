def Reverse(lst):
  new_lst = lst[::-1]
  return new_lst

class Solution(object):
  def isPalindrome(self, x):
    x = str(x)
    f = [x for x in x] 
    b = [x for x in x]
    b_r = Reverse(b)
    if (f == b_r):
      return True
    return False

new_solution = Solution()

print(new_solution.isPalindrome(12))