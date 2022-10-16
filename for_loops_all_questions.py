#In math, the factorial of a number is defined as the product of an integer and all the integers below it. For example, the factorial of four (4!) is equal to 1*2*3*4=24. Fill in the blanks to make the factorial function return the right number.

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

# ----------##----------

#The validate_users function is used by the system to check if a list of users is valid or invalid. A valid user is one that is at least 3 characters long. For example, ['taylor', 'luisa', 'jamaal'] are all valid users. When calling it like in this example, something is not right. Can you figure out what to fix?

def validate_users(users):
  for user in users:
    if is_valid(user):
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(["purplecat"])

# ----------##----------

#Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.

def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
    return result

for n in range(0,10):
    print(n, factorial(n+1))
