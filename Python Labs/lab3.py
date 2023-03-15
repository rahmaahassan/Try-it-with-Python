'''
Write a function that accepts two arguments (length, start)
to generate an array of a specific length filled with integer 
numbers increased by one from start.
'''

def fun(start, length):
   return list(range(start, start+length))

start = int(input("Enter the  start: "))
length = int(input("Enter the length : "))
print(fun(start,length))

'''
write a function that takes a number as an argument and if the number
divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz"
and if is is divisible by both return "FizzBuzz"
'''

def return_it(num):
   if (num % 3 == 0) and (num % 5 ==0):
      return 'FizzBuzz'
   elif num % 3 == 0:
      return 'Fizz'
   elif num % 5 ==0:
      return 'Buzz'
   else:
      return num
   
num = int(input('Enter your number: '))
print(return_it(num))

'''
Write a function which has an input of a string from user then
it will return the same string reversed.
'''

def reverse(str):
    t = ''
    for i in str:
       t = i+t
    return t  
str = input('Enter your String: ')  

# or
def reverse_simple(str):
   return str[::-1] 

print(reverse(str))

'''
Ask the user for his name then confirm that he has entered his 
name(not an empty string/integers).
then proceed to ask him for his email and print all this data 
check if it is a valid email or not 
'''

import re

regex = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

name = input('Enter your name: ')
while name != '' or name.isdigit():
    email =input("Enter your email: ")
    if re.match(regex,email):
        print("Valid Email")
        print(name)
        print(email)
    else:
        print("Invalid Email")
        

'''
Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For 
example, if the string is 'abdulrahman' then 
the output is: Longest substring in alphabetical order is: abdu
'''

def long_str(str):
    longest = str[0]
    current = str[0]
    for char in str[1:]:
        if char >= current[-1]:
            current += char
        elif len(current) > len(longest):
            longest = current
        else:
            current = char
    return longest

str = input('Enter the string: ')
print(long_str(str))

# another try

import re

def long_str (str):
    substrings = re.findall('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*', str)
    return max(substrings, key=len)

str = input('Enter the string: ')
print(long_str(str))

'''
Write a program which repeatedly reads numbers until the user enters “done”.
○ Once “done” is entered, print out the total, count, and average of the numbers.
○ If the user enters anything other than a number, detect their mistake, 
  print an error message and skip to the next number.
'''

count = 0
total = 0
while True:
    num = input('Enter the namber: ')
    if num == 'done':
        break
    try:
        no = int(num)
    except:
        print('Enter Valid Number!')
        continue
    count+=1
    total+= int(no)
print('total number: ', total)
print('count number: ', count)
print('average number: ', total / count)

'''
Word guessing game (hangman)
'''

import random

name = input('Enter Your Name: ')
words = ['apple', 'car', 'mouse', 'girl', 'book', 'cinema']

word = random.choice(words)
print("Guess the characters")

guesses = ''
turns = 7

while turns > 0:
    count = 0
    for char in word:
        if char in guesses:
            print(char, ' ')
        else:
            print('_')
            count +=1
    if count == 0:
        print('Great job, you win! ', name)
        print("The word is: ", word)
        break

    guess = input('Guess a character: ')
    guesses += guess
    if guess not in word:
        turns -=1
        print('Try again')
        print('you have ', +turns, 'more gusses')
        if turns == 0:
            print('you lose!!!')