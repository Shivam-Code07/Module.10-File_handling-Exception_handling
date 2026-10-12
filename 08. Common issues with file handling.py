# '''
# we are gonig to leearn few common error in file handling.
# using mode (x,a,r,w)
# '''


### Read Mode
# fh = open("learning.txt","rt")
# #FileNotFoundError: [Errno 2] No such file or directory: 'learning01.txt'
# # contents = fh.read()
# fh.write("some content") # io.UnsupportedOperation: not writable
# fh.close()
# # print(contents)
# '''
# if you are open a file read mode you can only read.
#  and u can use some read function like read, readline or readlines'''

### Write Mode
# fh = open("learning.txt","wt")
# content = fh.read() # io.UnsupportedOperation: not readable
# 'if you are open any file in write mode, it will going to delete all the content. '
# 'whatever present in the .txt file here we are getting error but content was deleted by w mode '
# fh.close()
# print(content)

# ### Create Mode
# fh = open("learing01.txt","xt") # if once a file created by create mode then you can use x mode again and again.
# #FileExistsError: "it will show you file existing error "
# fh.write("hey, this file created by create mode in python.")

# content = fh.read()
# print(content)

# 'you can not read a file in x mode if a file exist. '
# fh.close

# ### Append Mode
# 'you can not read, if you open a file append mode'
# fh = open("learing01.txt","at")
# content = fh.read() #io.UnsupportedOperation: not readable
# print(content)

python_file = open("10. Exception handlig - else & finally.py","xt")
python_file.write("'''This is the 1st Python file, Which i create through 'x' mode .\n")
python_file.write("See soon..'''")
contents = python_file.readlines()
python_file.close()
print(contents)   # Here is the most important thing is "you can not use x mode and r mode at a same time"
# io.UnsupportedOperation: not readable " most probably you got this error"
