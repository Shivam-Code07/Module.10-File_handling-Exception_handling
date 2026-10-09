# # os.path.exists()
# import os

# file_name = "/Users/bittu/Python/Module 10 (File handling  Exception handling)/learning.txt"

# if os.path.exists(file_name):
#     print("File exist")
# else:
#     print("File does not exist")    








# os.path.exists()
from pathlib import Path

file_name = Path("/Users/bittu/Python/Module 10 (File handling  Exception handling)/learning_1.txt")

if file_name.exists():
    print("File exist")
else:
    print("File does not exist\nwe are just creating.....")    
    fh = open(file_name,"xt")
    fh.write("this file create using os.path.exists()\n")
    fh.write("good bye!!\n")
    fh.write("see you soon.......")
    fh.close()