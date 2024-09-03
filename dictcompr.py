#dict comprehension allow you to create a new dict by iterating over an exisiting 
#specifying key values pair
#syntax'{key_expression: value_expression for item in iterable if condition}
#create a dictonary of square numbers range 1-5
square_nums=[x**2 for x in range(1,5)]
print(square_nums)
# redo with dictonary comprenssion
keys=['a','b','c','d','e']
values=[1,2,3,4,5]
dictionary={k:v for k, v in (zip(keys,values))}
print(dictionary)