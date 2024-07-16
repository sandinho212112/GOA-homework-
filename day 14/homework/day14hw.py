#for loop tasks

#all integers from 0 to 20 inclusive
for i in range(21):
    print(i)

#the first 10 natural numbers.
for i in range(1, 11):
    print(i)

#task:Print even numbers separately and odd numbers separately from 0 to 100 inclusive:
print("Even numbers:")
for i in range(0, 101, 2):
    print(i)

print("Odd numbers:")
for i in range(1, 101, 2):
    print(i)

#Enter a number to the user and then using a for loop output the sum of all the numbers up to this number
num = int(input("Enter a number: "))
total_sum = 0
for i in range(1, num + 1):
    total_sum = i
print("The sum of all numbers up to", num, "is", total_sum)

#Write an algorithm that prints multiples of 5 (numbers divisible by 5) from 1 to 50 inclusive
for i in range(5, 51, 5):
    print(i)

 #for loop
 # Print even numbers up to 20
i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1   

#Calculate the sum of numbers from 1 to 10
i = 1
total_sum = 0
while i <= 10:
    total_sum += i
    i += 1
print("The sum of numbers from 1 to 10 is", total_sum)    

#Write a while loop that asks the user to guess a number between 1 and 10 until they get it right. The correct number is 7
correct_number = 7
guess = -1
while guess != correct_number:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != correct_number:
        print("Wrong guess, try again!")
print("Congratulations! You guessed the correct number.")

#Write a while loop that processes a list of numbers, doubling each number, and prints the new list
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    numbers[i] *= 2
    i += 1
print("Doubled numbers:", numbers)

#Write a while loop that repeatedly asks the user to enter a password until the correct password "password123" is entered:
correct_password = "password123"
password = ""
while password != correct_password:
    password = input("Enter the password: ")
    if password != correct_password:
        print("Incorrect password, try again.")
print("Access granted.")

#Write an if-else statement that prints "Good morning!" if the current hour is less than 12 and "Good afternoon!" otherwise
import datetime

current_hour = datetime.datetime.now().hour

if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")

#Write an if-else statement that checks if a number is even or odd. If the number is even, print "Even"; otherwise, print "Odd"
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Create an if-else statement to check if the temperature is above 30 degrees. If it is, print "It's hot outside!"; otherwise, print "It's not too hot"
temperature = float(input("Enter the temperature: "))

if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

#Create an if-else statement that determines if a person is a teenager. If the age is between 13 and 19 (inclusive), print "You are a teenager!"; otherwise, print "You are not a teenager"
age = int(input("Enter your age: "))

if 13 <= age <= 19:
    print("You are a teenager!")
else:
    print("You are not a teenager.")

#for loop
#Write a program that calculates and prints the sum of numbers from 1 to 10 using a for loop
total_sum = 0
for i in range(1, 11):
    total_sum += i
print("The sum of numbers from 1 to 10 is", total_sum)

#Print the squares of numbers from 1 to 15
for i in range(1, 16):
    print(f"The square of {i} is {i**2}")


#Write a program that calculates and prints the sum of squares of numbers from 1 to 5 using a for loop              
sum_of_squares = 0
for i in range(1, 6):
    sum_of_squares += i**2
print("The sum of squares of numbers from 1 to 5 is", sum_of_squares)

#Print numbers divisible by both 3 and 5 from 1 to 100 inclusive
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

#Write a program that prints numbers from 10 to 1 in reverse order using a for loop
for i in range(10, 0, -1):
    print(i)


#while loop
#Calculate the sum of digits of a number entered by the user            
number = int(input("Enter a number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print("The sum of the digits is", sum_of_digits)


#Write a program that uses a while loop to print numbers from 10 down to 1
i = 10
while i > 0:
    print(i)
    i -= 1

#Write a program that calculates and prints the sum of all integers from 1 to 100 using a while loop
i = 1
total_sum = 0
while i <= 100:
    total_sum += i
    i += 1

print("The sum of all integers from 1 to 100 is", total_sum)

#Write a program that calculates and prints the square of numbers from 1 to 10 using a while loop
i = 1
while i <= 10:
    print(f"The square of {i} is {i**2}")
    i += 1

#if else
#Write an if-else statement to determine if a year entered by the user is a leap year
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Check if a given string entered by the user is a palindrome

string = input("Enter a string: ")

if string == string[::-1]:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")


#Determine if a number entered by the user is positive, negative, or zero

number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#Calculate the BMI of a person based on their height and weight entered by the user and classify their BMI category using if-else
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")    
