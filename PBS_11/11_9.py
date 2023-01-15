Array=eval(input("Enter a list:"))
Mode=0
Large=0
for x in Array:
    sm=0
    for i in range (len(Array)):
        if Array[i]==x:
            sm+=1
        if sm>Large:
            Large=sm
            Mode=x
print("The mode of given list is",Mode)
