"""name= input('Please enter your name? ')
colour= input('Please enter your favorite color? ')
print(name + ' likes ' + colour)"""

"""birth_year=input('Please enter your birth year: ')
age = 2024 - int(birth_year)
print(age)"""

"""weight_pounds= input('Please enter your weight in pounds: ')
weight_kg=int(weight_pounds)*0.45
print(weight_kg)"""

"""name='jeniffer'
print(name[1:-1])"""

"""first_name='Hayyan'
last_name='Mohamed'
print(f'{first_name} [{last_name}] is a coder')"""

"""course='python for beginners'
print(course.replace('p','q'))"""


"""import math
print(math.floor(2.9))"""


"""price=1000000
good_credit=True
if good_credit:
    downpayment=0.1*price
else:
    downpayment=0.2*price
print(f"downpayment:{downpayment}")"""

"""has_high_income=True
has_good_credit=True
if has_high_income and has_good_credit:
    print('Eligible for loan')"""

temperature=35
if temperature>30:
    print("its a hot day.")
elif temperature<30:
    print('its a cold day')
else:
    print('its neither hot or cold')

name=input('Please enter your name: ')
name=int()
if len(name)<3:
    print('Nmae must be three characters long')
elif len(name)>50:
    print('names must be less than 50 characters.')
else:
    print('name looks good')
