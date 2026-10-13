'''This is the 1st Python file, Which i create in 'x' mode .
See you soon..'''
import io
# Hi, in the previous .py file i learn about try & except
try:
    with open("file_01.txt","wt") as fh: 
        fh.write("Some Content")
        # data = fh.read()
        # print(data)
except FileNotFoundError as file_error: ## This block will execute only if the try block not runs successfully.
    print("File doesn't exist.")  
    print(file_error)
except io.UnsupportedOperation as io_error:
    print(io_error)
else: # This block will execute only if the try block runs successfully without any errors.
    print("Else Block")
finally: ## This block will execute everytime without any errors.
    print("Finally Block")


    '''
    One thing you can noticed easyly else block only run if try block run without any error.
    if try block face any type of error or if except block run .
    else block doesn't run.
    '''