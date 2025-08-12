def checkkthbit(n,k):
    if ((n&(1<<k))==0):
        return False
    return True
n=int(input())
k=int(input())
print(checkkthbit(n,k))