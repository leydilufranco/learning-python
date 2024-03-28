

sum_two_value = lambda first_value, second_value: first_value + second_value
print(sum_two_value (2,4))

mulriply_values = lambda first_value, second_value: first_value * second_value -3 
print(mulriply_values(2, 4))

def sum_three_values (value):
    return lambda first_value, second_value: first_value + second_value * value

print (sum_three_values (5)(2, 4))