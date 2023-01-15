Array=eval(input("Enter a list:"))
l=-1
for a in Array:
    if a%2==0 and a>l:
        l=a
if l!=-1:
    print("The largest even number in the given list is:",l)
else:
    print("There is no even element in the given list !!!")