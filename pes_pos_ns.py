
print("#program to program a program to print sum of even pos. no.,odd pos. no., neg. no. differently.\n ENTER 0 TO END")
pes=pos=ns=penct=ponct=nnct=0
while True :
    n=int(input("enter a number:"))
    if n>0:
        if n%2==0:
            penct+=1
            pes+=n
        else:
            ponct+=1
            pos+=n
    elif n<0:
        nnct+=1
        ns+=n
    else:
        break
print("="*60)
print("YOU ENTERED:\nNegative numbers:",nnct,
"\tPositive even number:",penct,"\tpositive odd number:",ponct,
"\nSum of positive even numbers:",pes,
"\nSum of positive odd numbers:",pos,
"\nSum of negative numbers:",ns)



