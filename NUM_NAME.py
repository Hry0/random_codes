num=int(input("enter a number :"))
pv=[10000000,100000,1000,100,90,80,70,60,50,40,30,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
wd=["crore","lakh","thousand","hundred","ninty","eighty","seventy","sixty","fifty","forty","thirty","twenty","nineteen","eighteen","seventeen","sixteen","fifteen","fourteen","thirteen","twelve","eleven","ten","nine","eight","seven","six","five","four","three","two","one"]
wordnum=""
i=0
while num>0:
    prefix=""
    s=0
    if num<100:
        if num>=pv[i]:
            wordnum+=wd[i]
            wordnum+=" "
            num-=pv[i]
    elif num>=100:
        if num>=pv[i]:
            s=num//pv[i]
            s2=s
            if s<=20:
                prefix=wd[s*-1]
            elif s<100:
                j=0
                while s>0:
                    if s>=pv[j]:
                        prefix+=wd[j]
                        prefix+=" "
                        s-=pv[j]
                    j+=1
            wordnum+=prefix
            wordnum+=" "
            wordnum+=wd[i]
            wordnum+=" "
            num-=pv[i]*s2
    i+=1
x=wordnum.title()
print(x)
