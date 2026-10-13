# # raising
# salary = float(input("Enter your salary: "))
# if salary < 0:
#     raise ValueError ("Salary can not be negative.\n\tTry again!!")
# else:
#     print(f"Your salary is: ₹{salary}")



# age = float(input("Enter your age: "))
# if age<0 :
#     raise ValueError ("Age can not be negative.Try Again!!!")
# elif age>125:
#     raise ValueError ("Age can not be more than 120.Try Again!!!")
# else:
#     if age<=18:
#         print("You can not cast your vote. \n you are not an adult.")
#     else:
#         print("Congrats! you are an adult.\n you can vote. ")

# if you no idea about or don't want remember all the error name 
# you can simpaly use "Exception" every where.

age = float(input("Enter your age: "))
if age<0 :
    raise Exception ("Age can not be negative.Try Again!!!")
elif age>125:
    raise Exception ("Age can not be more than 120.Try Again!!!")
else:
    if age<=18:
        print("You can not cast your vote. \n you are not an adult.")
    else:
        print("Congrats! you are an adult.\n you can vote. ")