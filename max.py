a=float(input("enter the first number:"))
b=float(input("enter the second number:"))
print("="*78)
if a>b:
    print(a, "is greater than",b)
    print(b, "is smaller than",a)
elif a==b:
    print(a,"=",b)
else:
    print(b, "is greater than",a)
    print(a, "is smaller then",b)
