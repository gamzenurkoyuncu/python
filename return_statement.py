# return statement = Functions send Python values/objects back to the caller.
#                     These values/objects are known as the function's return value

def multiply(number1,number2):
    result = number1*number2
    return result
    return number1*number2 # for the less lines of code

x = multiply(2,3)
print(x)

multiply(2,3)
print(multiply(2,3))
