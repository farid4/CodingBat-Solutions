def array_count9(nums):
  count = 0
  
  for i in range (len(nums)):
    if nums[i] == 9:
      count +=1
      
  return count
