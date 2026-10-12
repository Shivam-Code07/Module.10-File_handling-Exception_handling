# we are going the learn -
# >>> Try or Expect funtion ! 
 
# in python we are geting some types of error.
# like: 1. Syntex Error
#       2. Indentation Error


# exception:> 'Error during execution'
# how to handle exceptions? => try-except block


try:
    num1 = float(input("Enter Your Number: "))
    num2 = float(input("Enter Your Another Number: "))
    res = num1/num2
    print(f"Your Division is {res}.")
except ZeroDivisionError:# here we are geting zero division error now , we are fix it. (it's working for calculatio error.)
    print("Denominator should not be zero.")    
except ValueError:# and this except section dealing with value error with input function.
    print("Value should be Digits.")
