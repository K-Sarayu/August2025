def generate(curr_str,Open,Close,ans,n):
    if(Open+Close==2*n and Open==Close):
        ans.append(curr_str)
        return
    if(Open>n):
        return
    if(Close>Open):
        return
    generate(curr_str+"(",Open+1,Close,ans,n)
    generate(curr_str+")",Open,Close+1,ans,n)
def generateParenthesis(n):
    curr_str=""
    ans=[]
    Open=0
    Close=0
    generate(curr_str,Open,Close,ans,n)
    return ans
n=int(input())
print(generateParenthesis(n))