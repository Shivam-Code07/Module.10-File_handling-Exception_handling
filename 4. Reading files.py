file_handler = open("learning.txt","rt")
# read opretion


# read() => read the contents of the file as string(str)

# content = file_handler.read()
# content = file_handler.read(10) # this reads first 10 characters of the file.

#readline()
# content1 = file_handler.readline() # this reads only first line of the file.
# content2 = file_handler.readline() # this read 2nd line of file
# content3 = file_handler.readline() # this read 3rd line of file
# content4 = file_handler.readline() # if we have no line file this will print empty line
#readlines()
content = file_handler.readlines() # this reads all line of the file. store in the list all line as list of element with \n

# closing a file => close()
file_handler.close()


for lines in content:
    print(lines.rstrip('\n')) 
