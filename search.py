import os
req_path=input("enter path to search for files:")
fd=os.listdir(req_path)
req_ext=input("enter the extension you want to print:")
for each in fd:
  if each.endswith(req_ext):
     print(each)
