def checkprime(n):
    res=[] #res=list()
    temp=''
    count=0
    for i in range(1,n+1,1):
        if n%i==0:
            res.append(i)
    if len(res)==2:
        return"prime"
    else:
        return"not prime"
inp=int(input("Enter a value:"))
print(checkprime(inp))
