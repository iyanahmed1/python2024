h_letters=[]
for letters in 'human':
    h_letters.append(letters)
    print(h_letters)
#using a list comprehension
h_letters=[letter for letter in 'human']
print(h_letters)
#we can achieve the same results usinga a lamda expression
#with maps
letters=list(map(lambda x:x,'human'))
print(letters)
#list comprehensio allow you to create a new list by iterating over  an existing itenary
#and applying a condition or tansformation
#syntax -[expression for item in iterable if condition]
#create a list of square numbers from 1-5
square_numbers=[x**2 for x in range(1,6)]
print(square_numbers)

#create a list of even numbers from an exisiting file
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[x for x in numbers if x%2==0]
print(even_numbers)
#convert the following list into list comprension
fruits=['Mangoes','Oranges','Pineapple','Lemons']
new_fruits=[]
for n in fruits:
    new_fruits.append(n)
print(new_fruits)

fruits=['Mangoes','Oranges','Pineapple','Lemons','Mananasi']
new_fruits=[n for n in fruits]
print(new_fruits)
fruits=[n for n in fruits]
print(fruits)

#create a new list containg fruits with the letter M
#hint use a for loop
M_fruits=[n for n in fruits if n.startswith('M')]
print(M_fruits)
