from playsound import playsound
print("Guidelines to write a valid code:\n\
    *It must begin with a number\n\
    *It must have 8 characters\n\
    *It should have at least one special symbol")
pas=input("Enter the password to play the secret song:")
d=1
if len(pas)>=8:
    if pas[0].isdigit()!=True:
        d=0
    for i in pas:
        if (i!=" " and i.isalnum()!=True)!=True:
            d=0
        else:
            d=1
            break
else:
    d=0
if d==False:
    print("Access Denied")
    playsound("c:/users/acer/documents/py/denied.mp3")
else:   
    print("Access Granted")
    playsound("C:/users/acer/music/arcade.mp3")    

  
