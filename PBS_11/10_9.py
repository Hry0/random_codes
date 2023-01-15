word=input("Enter a string:")
word2=input("Enter anothe string:")
l1=len(word)
l2=len(word2)
if l1>l2:
    if word2 in word[:l2]:
        print(word2,"is a prefix of",word)
elif l2>l1:
    if word in word2[:l1]:
        print(word,"is a prefix of",word2)
else:
    print("neither is prefix of other")
