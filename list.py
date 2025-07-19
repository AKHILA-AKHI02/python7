def printlist(n):
    res=[]#res=list()
    for i in range (1,n+1,1):
        if n%i==0:
            res.append(i)
    return res
inp=int(input("Enter a number:"))
print(printlist(inp))
print("count of factors of",inp,"is",len(printlist(inp)))

