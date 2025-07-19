def sub(m,m1):
    z=m-m1
    return z
for i in range(100):
    n=int(input("Enter a number:"))
    n1=int(input("Enter a number:"))
    print(sub (n,n1))
    choice=input("To exit press c:")
    if choice=='C' or choice=='c':
        break
    
