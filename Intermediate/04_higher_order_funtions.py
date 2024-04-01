## Higher order Functions 

def sum_one (value):
    return value + 1

def mult_one (value):
    return value * 5

def sum_two_and_add_one (first_value, second_value, mul_value):
    return mul_value (first_value + second_value)

print (sum_two_and_add_one(2, 4, mult_one))

