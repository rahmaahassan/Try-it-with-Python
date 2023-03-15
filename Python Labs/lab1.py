'''
Write a program that counts up the number of vowels 
[a, e, i, o, u] contained in the string.
'''

name = input('Enter The String: ')
count = 0
for i in name:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i =='u'):
         count+=1
print('the count is', count)

'''
Write a program that prints the number of times 
the string 'iti' occurs in anystring.
'''

string = input('Enter The String: ')
count = string.count('iti')
print(count)

'''
Write a program that remove all vowels from 
the input word and generate a brief version of it.
'''

string = input('Enter The String: ')
vowels = ['a', 'e', 'i', 'o', 'u']
after_del = ''
for i in range(len(string)):
    if string[i] not in vowels:
        after_del = after_del + string[i]
print('the string after delete vowels: ', after_del)

'''
Write a program that prints the locations 
of "i" character in any string you added.
'''

string = input('Enter the string: ')
for i in range(len(string)):
    if string[i] == 'i':
        print(i)

'''
Write a program that build a Mario pyramid
'''

input = int(input('Enter the Input: '))
i=1
while (i <= input):
    print(' '*(input-i)+ '*' * i)
    i+=1