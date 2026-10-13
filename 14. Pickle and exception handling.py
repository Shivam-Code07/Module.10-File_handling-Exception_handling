import pickle
students = {'student1':{'roll':101, 'name':'Bittu', 'percent':90.49},
            'student2':{'roll':102, 'name': 'Shivam', 'percent':78.60},
            'student3':{'roll':103, 'name': 'Piyush', 'percent': 98.92}
}
print(students,type(students))

# serialization
with open("student_info01.bin","wb") as fh: #with open("student_info01.bin","bx") as fh:
    for student in students:
        pickle.dump(students[student],fh)

# deserialization 
# print the names of students who secured >=90 percent
list = []
with open("student_info01.bin","rb") as fh:
    while True:
        try:
            data = pickle.load(fh)
            print(data,type(data))
            if data['percent'] >= 90:
                list.append(data['name'])
                print(f"List of students who secured >= 90%: {list}")
        except EOFError:
            print("Done..")
            break

        










# with open("student_info01.bin","rb") as fh:
#     for student in students:
#         print(pickle.load(fh))
#         # print(pickle.load(fh))
#         # print(pickle.load(fh))
#         #print(pickle.load(fh))#. EOFError: Ran out of input