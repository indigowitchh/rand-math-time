import random
nums = []
nums2=[]

for i in range (12):
    nummies = random.randrange(1,11)
    nums.append(nummies)

nums.sort()
print(nums)
print("The smallest number is:",nums[0])
print("The largest number is:", nums[11])
 
for i in range(10):
    if nums[i]+1==nums[i+1]:
        if nums[i+1]+1 == nums[i+2]:
            print("The list contains,", nums[i], nums[i+1], nums[i+2])

for i in range (12):
    nums2.append(nums[11-i])
print("Original list:", nums)
print("Reversed list:", nums2)
