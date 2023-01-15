import random
st=input("Enter something to encrypt or decrypt:")
ed=input("Press:('E'-to encrypt 'D'-to decrypt):")
key=input("Enter a Key:")
st2=""
L="!@#$%^&*()))_+}{:'|~?><?~`/.,;'\\][=-``~]"
if ed=="E" or ed=="e":
    key=int(key)
    if key<200:
        key+=random.randint(100,300)
    pos=""
    r=random.randint(199,399)
    for i in range(len(st)):
        o=ord(st[i])
        if chr(o+key).isalnum() or chr(o+key) in L:
            st2+=chr(o+key)
        else:
            st2+=chr(o+r)
            pos+=i
            pos+="."
    key2=str(key)+"."+str(r)
    print("The encrypted message is:"+repr(st2)+"|\nFor Decription:\nKey=",key2,"positions=",pos)
elif ed=="D" or ed=="d":
    p=input("Enter positions:")
    pos=p.split(".")
    keys=key.split(".")
    key=int(keys[0])
    key2=int(keys[1])
    for i in range(len(st)):
        o=ord(st[i])
        if str(i) not in pos:
            st2+=chr(o-key)
        else:
            st2+=chr(o-key2)
    print("The decrypted message is:"+st2+"|")
else:
    print("Enter the correct option.")
print("😍😍😍😍💕💕💕😉😆😆😆😆🤣🤣🤣🤣🗯🕕🕛🔳🔸")
