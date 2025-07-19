def sum_of_digits(n):
    sd=0
    for i in n:
        sd=sd+int(i)
    return sd
inp=input("Enter a value:")
print(sum_of_digits(inp))
