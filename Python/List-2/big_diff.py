# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

def big_diff(nums):
  minimum =  nums[0]
  maximum = nums[0]
  for i in range (1,len(nums)) :
    minimum = min (minimum, nums[i])
    maximum = max (maximum, nums[i])
  return maximum - minimum
