st=input("Enter something to encrypt or decrypt:")
ed=input("Press:('E'-to encrypt 'D'-to decrypt):")
st2=""
if ed=="E":
    st2=""
    key=int(input("Enter a Key:"))
    enc=[]
    for i in st:
        enc.append(i)
    ct=""
    for i in range(len(st)):
        if (str(i)) not in ct:
            ct+=str(i)
            ct+=str(i+key)
            enc[i],enc[i+key]=enc[i+key],enc[i]
        st2+=enc[i+key]
        st2+=enc[i]
    print("The encrypted message is",st2)
elif ed=="D" or ed=="d":
    key=int(input("Enter a key:"))
    key=0
    key2=int(input("Enter the key2:"))
    for i in range(len(st)):
        key2-=key
        if i-key2>=0:
            st2+=[i-key2]
        else:
            st2+=len(st)-(i-key2)
            key=len(st)-(i-key2)

