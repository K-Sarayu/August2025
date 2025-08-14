def generate(ind,curr_subset,ans,candidates,target):
    if(target==0):
        ans.append(curr_subset.copy())
        return 
    if(target<0 or ind==len(candidates)):
        return
    curr_subset.append(candidates[ind])
    generate(ind,curr_subset,ans,candidates,target-candidates[ind])
    curr_subset.pop()
    generate(ind+1,curr_subset,ans,candidates,target)
def combinationSum(candidates,target):
    ind=0
    curr_subset=[]
    ans=[]
    generate(ind,curr_subset,ans,candidates,target)
    return ans
candidates=[2,3,6,7]
target=7
print(combinationSum(candidates,target))