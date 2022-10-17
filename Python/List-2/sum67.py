def sum67(nums):
  sum = 0
  found6 = False
  for i in range (len(nums)):
    if nums[i]==6:
      found6 = True
    if not found6:
      sum += nums[i]
    if nums[i] == 7 and found6 :
      found6 = False
  return sum
