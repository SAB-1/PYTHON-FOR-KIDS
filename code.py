### This project let you submit your bio-details and group you into categories according to your information

## Bio-data
first_name = input("What is your first name?")
last_name = input("What is your last name?")

full_name = first_name + " " + last_name

age = int(input("How old are you?"))

Gender = input(["Male", "Female"])

if Gender == "Male":
  print(f'This is {name}, He is {age} years old')
elif Gender == "Female":
  print(f'This is {name}, She is {age} years old')
else:
  print(f'Kindly look through your inputs')

## Categorizing your information according to age

if age <= 12:
  print('You are a Child')
elif 13 <= age <= 17 :
  print('You are a Teenager')
elif age >= 18:
  print('You are an Adult')

## getting to know the temperature

temperature = int(input('Enter measured temperature:'))
if temperature <= 20:
  print('It is cold')
else:
  print('It is warm')


# Arithmetic Challenge
print("\n Let's test your math skills!")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print(f"\nHere are some quick calculations with {num1} and {num2}:")
print(f"➕ Addition: {num1} + {num2} = {num1 + num2}")
print(f"➖ Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"✖️ Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"➗ Division: {num1} / {num2} = {num1 / num2:.2f}")
