'''
Fill an array of 5 elements from the user, 
Sort it in descending and ascending orders then display the output.
'''

list = []
i = 0
while i < 5:
	e = input('please enter a number: ')
	if e.isdigit():
		list.append(e)
	else:
		print('please input a number not anything else: ')
		i -= 1
	i += 1

print(list)

# sorted asc  
for i in range (len(list)):
	for j in range(i + 1, len(list)):
		if(list[i] > list[j]):
			list[i], list[j] = list[j], list[i]
			
print(list)

# sorted desc 
for i in range (len(list)):
	for j in range(i + 1, len(list)):
		if(list[i] < list[j]):
			temp = list[i]
			list[i] = list[j]
			list[j] = temp
print(list)

'''
Write a program that generate a multiplication table from 1 to the number passed.
'''

num = int(input("Enter the num: "))
list = []
for i in range(1, num+1):
   list1 = []
   for j in range(1, i+1):
      e = i*j
      list1.append(e)
   list.append(list1)
print(list)