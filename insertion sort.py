from rich import print
from rich import text
l=eval(input("enter a list:"))
print("+"*88)
print("original list is:",l)
def sort():
  for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and key<l[j]:
            l[j+1]=l[j]
        j=j-1
    else:
        l[j+1]=key
print("[blue]the list after insertion sort in ascending order is:[/]",l)
L=l[::-1]
print("\n[red]the list after insertion sort in desc order is:[/]",L)

int