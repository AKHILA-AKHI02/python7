def fun(n):
 for i in range(1,inp):
    if i%5==0:
        continue
    print(i,end=',')  
print("Executed")
inp=int(input("enter a value:"))
print(fun(inp))
