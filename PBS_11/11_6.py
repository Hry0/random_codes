Array=eval(input("Enter a List:"))
st=""
for x in Array:
    if x!=Array[len(Array)-1]:
        st+=str(x)+"-"
    else:
        st+=str(x)
print(st)