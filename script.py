import os
path=input("enter the path to list the directories and files: ")
fod=os.listdir(path)
for each in fod:
  
  x=(os.path.join(path,each))
  if os.path.isfile(x):
    print(f"{x} is a file")
  else:
    print(f"{x} is a directory")
  
