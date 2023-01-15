import pickle
file1=open("hellopic.dat","wb")
dict1={"hello":123}
pickle.dump(dict1,file1)