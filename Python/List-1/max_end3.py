def max_end3(nums):
  m=max(nums[0], nums[2])
  nums[0]=m
  nums[1]=m
  nums[2]=m
  return nums
