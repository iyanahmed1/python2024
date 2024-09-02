
#list
fruits=['Strawberry','Apple','Oranges','Grapes','Kiwi']
new_fruits=['Banana','Peaches']
fruits.extend(new_fruits)
fruits.remove('Grapes')
print(len(fruits))
print(fruits)
#dict
details={'Name':'Hayyan','Age':'20','City':'Mombasa'}
details.update({'Occupation':'Student'})
details.update({'Age':'21'})
print(details)
#type conversion
number=('20')
number=int('20')
print(number,type(number))
num1=(20)
num1=float(20)
print(num1,type(num1))
num2=(20.1)
num2=str(20.0)
print(num2,type(num2))



