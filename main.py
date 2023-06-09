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


num1 = int(input('Enter the first number : '))
num2 = int(input('Enter the second number : '))

def bigger(num1, num2) :
  if num1 > num2 :
    print(f'The Bigger Number is {num1}')
  else :
    print(f'The Bigger Number is {num2}')

bigger(num1, num2)