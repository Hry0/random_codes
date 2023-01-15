n=int(input("Enter the no. of rows:"))
s1=s2=(n+1)//2
for i in range(1,n+1):
    for j in range(1,((n+1)//2)*2):
        if j==s1 or j==s2:
            print("*",end="")
        else:
            print(end=" ")
    print()
    if n%2==0:
        if i<n//2-1:
            s1-=1
            s2+=1
        elif i==n//2 or i==n//2-1:
            s1=1
            s2=n-1
        else:
            s2-=1
            s1+=1
    else:
        if i<n//2+1:
            s1-=1
            s2+=1
        else:
            s1+=1
            s2-=1
