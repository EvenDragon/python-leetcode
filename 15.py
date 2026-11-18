nums = [-1,0,1,2,-1,-4]
nums = list(set(nums))
nums.sort()
ans = []
i,j,k = 0,1,len(nums)-1
while i<len(nums)-2:
    while j<k:
        x = nums[i] + nums[j] + nums[k]
        if x == 0:
            ans.append([nums[i], nums[j], nums[k]])
            break
        elif x < 0:
            j += 1
        elif x > 0:
            k -= 1
    i+=1
    j = i+1
    k = len(nums)-1
print(ans)
