# food_amount =  int(input('Enter Amount $ : '))
# print(f'The food amount is : $ {food_amount}')
# tip = int(input('Enter Tip : '))
# print(f'The tip is : $ {tip}')

# total = food_amount + tip
# print(f'The total amount is : $ {total}')


# weather = input('Whats the weather today ? ')

# if weather == 'raining' :
#   print('Grab An Umbrella')
# elif weather == 'sunny' :
#   print('Put on Your SunGlasses')
# else :
#   print('Stay Home')
  
# score = int(input('Whats your score mate? '))

# if score >= 90 :
#   print('Grade A')
# elif score >= 80 :
#   print('Grade B')
# elif score >= 70 :
#   print('Grade C')
# elif score >= 60 :
#   print('Grade D')
# else :
#   print('Grade F')


# def sum(a, b) :
#   return a + b

# sum(1, 2)

# def foodCalculator(foodAmount, tip) :
#   print(f'The food amount is : $ {foodAmount}')
#   print(f'The tip is : $ {tip}')
#   total = int(foodAmount) + int(tip)
#   return total

# print(f'The Total Amount is $ {foodCalculator(300, 200)} ')

# weather = input('Whats the weather today ? ')

# def weatherChecker(weather) :
#   if weather == 'raining' :
#     print('Grab An Umbrella')
#   elif weather == 'sunny' :
#     print('Put on Your SunGlasses')
#   else :
#     print('Stay Home')

# weatherChecker(weather)

# num1 = int(input('Enter the first number : '))
# num2 = int(input('Enter the second number : '))

# def bigger(num1, num2) :
#   if num1 > num2 :
#     print(f'The Bigger Number is {num1}')
#   else :
#     print(f'The Bigger Number is {num2}')

# bigger(num1, num2)


# fruits = ['banana' , 'apple', 'oramge']
# # print(fruits)
# fruits.append('strawberry')
# # print(fruits[2])
# print(fruits[0:3])


# Dictionary
# person = { 'name' : 'david',
#           'ambition' : 'software engineer',
#           'age' : '19',
#           'dream country' : 'germany' }

# print(person['name'])
# print(person['age'])
# print(person['ambition'])
# print(person['dream country'])


# def introducer():
#   person = {
#     'name' : 'david',
#     'ambition' : 'software engineer',
#     'age' : 19,
#     'dream_country' : 'germany' 
#   }

#   person['age'] = 20
#   print(f"Hi my name is {person['name']} im {person['age']} years old, my ambition in life is to become a very good {person['ambition']} and my dream country is {person['dream_country']}")

# introducer()

# # tuple
# numbers = (1,2)
# print(numbers)

# sets

# language1 = ['Javascript', 'python' , 'Java', 'python']
# language2 = ['Java', 'Javascript', 'sql', 'nodeJs', 'nodeJs']
# language3 = set(language1 + language2)
# print(language3)

# items = ['sql', 'sql', 'node']
  
# def unique(items):
#   return (list(set(items))) 

# print(unique(items))

# loops
fruits = ['banana' , 'apple', 'oramge', 'paw paw']

# for fruit in enumerate(fruits):
#   print(f'Fruit : {fruit} ')

# # tupel unpacking
# for index, fruit in enumerate(fruits):
#   print(f'Fruit : {fruit} {index}')

#  range

# for _ in range(5):
#   fruits.append('orange')

# print(fruits)


# # while loops
# counter = 0

# while counter < 10 :
#   print(counter)
#   counter = counter + 1


# # double number
# def double_number(numbers):
  
#   result = []
#   result.append(numbers * 2)
#   return result

#  # result = numbers * 2
#  # return result         this approach also works


# print(double_number(100))

# # count word

# def count_word(words):
#   print(len(words.split()))

# count_word('Hello David')


# def sum_list(numbers):
#   count = 0
#   for number in numbers:
#     count += number

#   return count

# print(sum_list([1, 2, 3]))
# print(sum_list([1, 2, 3, 4]))



# def find_max(numbers):
#   current_max = numbers[0]
#   for number in numbers:
#     if number > current_max:
#       current_max = number

#   return current_max

# print(find_max([1, 2, 3, 10, 17, 4, 5, 6]))


# # dictionary practice
# def word_frequency(phrase):
#   result = {}
#   words = phrase.split() 
#   for word in words:
#     if word not in result:
#       result[word] = 1
#     else:
#       result[word] += 1
#   return result

# print(word_frequency(input('Enter words : ')))
      
  
# Higher order functions
# map
# filter



# list comprehensions

numbers = [1,2,3,4,5,6,7,8,9,10]

# filter and print even numbers
print([number for number in numbers if number % 2 == 0])

# map and double numbers
print([number * 2 for number in numbers])

# filter and print odd numbers
print([number for number in numbers if number % 2 != 0])

# filter and print odd numbers squared
print([number ** 2 for number in numbers if number % 2 != 0])

# filter and print odd numbers cubed
print([number ** 3 for number in numbers if number % 2 != 0])

# print maximum numbers
def my_max():
  num = input('enter numbers : ')
  print(max(num))

my_max()


### SPECIAL BUILT-IN FUNCTIONS with Python ###
# >>> sum([1, 2, 3])
# 6
# >>> len([1, 2, 3])
# 3
# >>> max([1, 2, 3])
# 3
# >>> max([1, 2, 3, 10, 5, 7])
# 10
# >>> min([1, 50, -7, 337])
# -7
