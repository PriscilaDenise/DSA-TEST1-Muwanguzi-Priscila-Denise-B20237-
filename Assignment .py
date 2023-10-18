

import math
#QN 1
# Prompt user to input value in degrees.
degrees = float(input('Enter a number:'))
radians = degrees * math.pi/180
# output the value in radians
print(radians)

# QN 2
# create list to hold the values 
values = []
# input the value of length and height
Length_of_base = float(input('Enter the length:'))
Height_of_parallelogram = float(input('Enter the height'))
# put the values in the list
values.append(Length_of_base)
values.append(Height_of_parallelogram)
# output the value
print(math.prod(values))

#QN 3
n = int(input('Enter a number:'))
factors = list(range(1,n + 1))

smallest_multiple = math.prod(factors)

print(factors)
print(smallest_multiple)

