# define a function that accepts a string as input and uses the for
# # loop to iterarete through the string and count the vowel      
def word(name):
    count=0
    vowel =("a","e","i","o","u")
    for i in name:
        for b in vowel:
            if i==b:
                count+=1        
    return count
print(word ("joyecs"))

# Write a Python function that takes two arguments (a and b) 
# and returns their sum.

def adition(a,b):
    return a+b
num1=70
num2=50
print (adition(num1,num2))



# Write a Python function that takes a 
# string as input and returns the string reversed.
def reversed_string(text):
    return text[::-1]
print(reversed_string("word"))
 # Write a Python function that takes a list of integers
#  as input and returns the sum of all the integers in the list.
def list_of_integers(ints):
    sum = 0
    for i  in ints:
        sum+=i
    return sum
print(list_of_integers([1,3,4,6,7,8]))


# Write a Python function that takes a list of integers
# as input and returns a new list with all the even numbers removed.
def even_numbers(intergers):
    list=[]
    for i in intergers:
        if i %2 != 0:
            list.append(i)

    return list
print(even_numbers([3,2,4,7,5,6,8,9,10,11]))





# Write a Python function that takes a list of integers 
# as input and returns the highest value in the list.
def list_of_integers(numbers):
    new=max(numbers)
    return new
print(list_of_integers([3,4,5,67,8,90,23,4,5]))

        



# Write a Python function that takes a list of strings as 
# input and returns a new list with all the strings capitalized.
def list_of_strings(names):
   namin=names.upper()
   return namin
print(list_of_strings("hopers"))
