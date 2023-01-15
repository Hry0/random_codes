from rich import print
n=int(input("Enter any number:"))
num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
sym=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
ro=""
i=0
while n>0:
    if n>=num[i]:
        ro+=sym[i]*(n//num[i])
        n-=num[i]*(n//num[i])
    i+=1
print(ro)