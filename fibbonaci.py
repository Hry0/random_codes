n=int(input("enter the no. of fibbonaci to be generated: "))
s=0
f=1
if n>=0:
    print(s,end=", ")
    if n>=1:
        print(f,end=', ')
        for i in range(1,n-1):
            s2=f
            f+=s
            print(f,end=", ")
            s=s2

