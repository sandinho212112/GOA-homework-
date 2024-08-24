#1
nums = [5,7,10,3,2,8]
copy_nums=nums[5:6]
print(copy_nums)
print(nums)

#2
nums = [5,7,10,3,2,8]
copy_nums=nums[0:3]
print(copy_nums)
print(nums)

#3
nums = [5,7,10,3,2,8]
copy_nums=nums[::2]
print(copy_nums)
print(nums)

#4
nums = [5,7,10,3,2,8,9]
copy_nums=nums[3:6]
print(copy_nums)
print(nums)

#5
nums = [5,7,10,3,2,8,9,4]
copy_nums=nums[0:4]
print(copy_nums)
print(nums)

#6
nums = [5,7,10,3,2,8,9,4]
copy_nums=nums[4:8]
print(copy_nums)
print(nums)

#7
nums = [5,7,10,3,2,8,9,4]
copy_nums=nums[1:-1]
print(copy_nums)
print(nums)

#8
nums = [5,7,10,3,2,8,9,4]
copy_nums=nums[2::3]
print(copy_nums)
print(nums)



#with strings now
#1
strs= "Sandro"
copy_strs=strs[0:3]
print(copy_strs)
print(strs)

#2
strs= "Sandro"
copy_strs=strs[::-1]
print(copy_strs)
print(strs)

#3
strs= "Sandro"
copy_strs=strs[::-1]
reversed_strs=copy_strs[::2]
print(copy_strs)
print(reversed_strs)
print(strs)

#copy da clear
#1
nums = [1,2,3,4,5,6,7,8]
numbers_clear=nums.clear()
print(numbers_clear)
print(nums)
#2
nums = [1,2,3,4,5,6,7,8]
numbers_clear=nums[:]
print(numbers_clear)
print(nums)
#3
nums = [1,2,3,4,5,6,7,8]
numbers_copy=nums.copy()
print(numbers_copy)
print(nums)