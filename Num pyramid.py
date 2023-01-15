a=int(input("enter the number of rows in pattern(enter odd no. only):"))
n=a//2+1
space=n
i=1
while i<=2*n+2:
    print(" "*space,end="")
    j=1
    while j<=i:
        if j <=i//2:
            for k in range(1,i//2):
                print(k,end="")
            j+=i//2
        else:
            for k in range(i//2,0,-1):
                print(k,end="")
            j+=i//2
        j+=1
    print()
    space-=1
    i+=2
i=2*n-1
space=1
while i>=1:
    print(" "*space,end="")
    j=1
    while j<=i:
        if j <=i//2:
            for k in range(1,i//2):
                print(k,end="")
            j+=i//2
        else:
            for k in range(i//2,0,-1):
                print(k,end="")
            j+=i//2
        j+=1
    print()
    space+=1
    i-=2