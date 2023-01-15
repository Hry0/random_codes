s=input("Enter any string:")
c=input("Enter any letter of string:")
s2=""
for i in s:
    if i==c:
        s2+=c.upper()
    else:
        s2+=i
print("The new string produced is:",s2)