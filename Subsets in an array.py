def subsets(nums):
    n=len(nums)#n=3; nums=[2,3,4]
    total_subsets=(1<<n)
    ans=[]
    for num in range(total_subsets):
        temp=[]
        for i in range(n):
            if((num&(1<<i))!=0):
                temp.append(nums[i])
        ans.append(temp)
    return ans
nums=[2,3,4]
print(subsets(nums))