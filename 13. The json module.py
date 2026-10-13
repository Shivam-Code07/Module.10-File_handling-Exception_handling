import json

students = {'student1':{'roll':101, 'name':'Bittu', 'percent':89.49,'sports':True},
            'student2':{'roll':102, 'name': 'Shivam', 'percent':83.78,'sports':False},
            'student3':{'roll':103, 'name': 'Piyush', 'percent': 80.82,'sports':False}
            }
print(students,type(students))
'''
# dump

with open("student.json",'w') as fh:
    json.dump(students,fh,indent=4) # for simplify your data in json file.
'''

'''
#load 
with open("student.json",'r') as fh:
    data = json.load(fh)
    print(data,type(data))
'''
# update 
#>>>> Read the old data from the .json file
try:
    with open("student.json",'r') as fh:
        data = json.load(fh)
except FileNotFoundError:
   with open("student.json",'x') as fh:
    json.dump(students,fh,indent=4)
else:
    #>>>> update opration
    data.update(students)

    #>>>> write the updated data in the json file
    with open("student.json",'w') as fh:
        json.dump(data,fh,indent=4)

