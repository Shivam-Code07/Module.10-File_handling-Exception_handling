# traditinal methode

fh = open("learn_1.txt", "rt")
content = fh.read()
fh.close

print(content)

# # # modern methode:-
# # # read()
# # with open("learn_1.txt","rt") as fh: 
# #     content = fh.read()

# # print(content)    

# #write()
# with open("learn_2.txt","wt") as fh: 
#     fh.write("This file created with help of 'with' function \n")
#     fh.write("bye!!!!")

