Array=eval(input("Enter a list:"))
sm=0
for x in range(len(Array)):
    if x%2==0:
        sm+=Array[x]
    else:
        sm-=Array[x]
print("The required sum is",sm)
