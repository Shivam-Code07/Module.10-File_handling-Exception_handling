# opening a file in python we have 'open()' function:
#- And also we have  some mode to open any file 
# altough open function have by default mode, which is open a file in read mode as a text file.

# mode >>>>. 
# r, w, a, x, t, b


#.  open(file_name, mode_to_open)

file_handler = open("learning.txt","rt")

print(file_handler)


file_handler.close()


print(file_handler)