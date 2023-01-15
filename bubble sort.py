# bubble sort
from rich import print
List=eval(input("enter the list to be sorted:"))
print("="*78)
n=len(List)
for i in range(n):
    for j in range(n-i-1):
        if List[j]>List[j+1]:
            List[j],List[j+1]=List[j+1],List[j]
print("The list after sorting is:",List)
#%%
# %%
