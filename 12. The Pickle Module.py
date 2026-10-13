# # Pickle Module
# # we are going to learn pickle module in python with example of dict. '{}'.
# students = {'student1':{'roll':101, 'name':'Bittu', 'percent':89.49},
#             'student2':{'roll':102, 'name': 'Shivam', 'percent':78.60},
#             'student3':{'roll':103, 'name': 'Piyush', 'percent': 98.92}
# }
# # print(students,type(students))


# # with open("student_info.txt","wt") as fh:


# #     fh.write(students) #TypeError: write() argument must be str, not dict
    
# #     # here we can not write a dict directly
# #     # then we can try to 1st convert dict inti str and the try kar sakte hai write karne ke liye
# student01 = str(students)
# with open("student_info.txt","wt") as fh:
#     fh.write(student01)

# with open("student_info.txt",'rt') as fh:
#     data =  fh.read()
#     print(type(data))


#     out = dict(data) #ValueError: dictionary update sequence element #0 has length 1; 2 is required
#     print(out)
# #>>>>>. Now let's try to fix it .
# # here is main thing







'''The main hero comes in to picture
the Hero is "pickle". 
'''
import pickle
students = {'student1':{'roll':101, 'name':'Bittu', 'percent':89.49},
            'student2':{'roll':102, 'name': 'Shivam', 'percent':78.60},
            'student3':{'roll':103, 'name': 'Piyush', 'percent': 98.92}
}
print(students,type(students))

# serialization
with open("student_info01.bin","wb") as fh: #with open("student_info01.bin","bx") as fh:
    for student in students:
        pickle.dump(students[student],fh)

# deserialization 
with open("student_info01.bin","rb") as fh:
    # for student in students:
        print(pickle.load(fh))
        print(pickle.load(fh))
        print(pickle.load(fh))
        #print(pickle.load(fh))#. EOFError: Ran out of input