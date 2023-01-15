n=int(input("Enter the no. of rows(you must enter a odd no.):"))
s1=s2=n//2
for i in range(n):
    for j in range(n):
        if j>=s1 and j<=s2:
            print("*",end="")
        else:
            print(end=" ")
    print()
    if i<n//2:
        s1-=1
        s2+=1
    else:
        s1+=1
        s