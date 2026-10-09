# 'x' mode >>> creating a file 
fh = open("file03.txt","xt")

# writing in to a file:
# 'w' mode >>> write(content)
fh.write("This file is created with the help of 'x' mode in python\n next line. ")
fh.write("And also we are writing with help of 'w' mode. ")


# close this file
# fh.close()
fh.write("\ntest content")
fh.close()