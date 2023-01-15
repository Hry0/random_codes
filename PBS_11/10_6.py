word=input('ENTER A WORD:')
l=len(word)
word2=''
sub=input("enter any letter to count in the given word:")
subct=0
for i in range(l):
    print(word[i],end=" | ")
    print(word[-i-1])
    word2+=word[-i-1]
    if word[i]==sub:
        subct+=1
print("Reversed word is:",word2)
print("The given letter '".upper()+sub+"' appeared in the word".upper(),subct,"times")