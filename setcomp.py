"""#set comprehension allow you to create a new set by iterating over an exisiting iterable
#syntax-'{expression for an item in iterable if condition}
# create a list of unique even numbers from an existing file
nums=[12,2,3,4,5,6,7,8,8,9,10,11,22,2,24]
unique_even= {x for x in nums if x%2==0}
print(unique_even)
#create a set of unique vowels from the string"Hello World"
stri='Hello,World'
vowels={char.lower() for char in str if char.lower() in 'aeiou'}
print(vowels)"""""

#create a set i prime numbers from range 2 to 20
start=2
end=20
nums={num for num in range(start, end+1)
       if all (num% i !=0 for i in range(2,int(num**0.5)+1))}
print(nums)
