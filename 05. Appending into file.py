# # 'a' => append function

# fh = open("file02.txt",'at')
# fh.write("This content has been written usind 'a' mode.\n")
# fh.write("'a' mode is used to add new content at the end of file.")
# fh.write("Good bye")
# fh.close()

# if the file does not exist, 'a' mode create the file.
fh = open("file05.txt",'at')
fh.write("This file has been created usind 'a' mode.\n")
fh.write("'a' mode create file if not already existing.\n")
fh.write("Good bye")
fh.close()