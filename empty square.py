n=int(input("Enter the number of rows in the pattern:"))
s1=s2=n//2+1
for i in range(1,n+1):
    for j in range(1,n+1):
        if j>=s1 and j<=s2:
            if j>n//4+1 and j<n-n//4 and i>n//4+1 and i<n-n//4:
                print(end=" ")
            else:
                print("*",end="")
        else:
            print(end=" ")
    if i<n//2+1:
        s1-=1
        s2+=1
    else:
        s1+=1
        s2-=1
    print()