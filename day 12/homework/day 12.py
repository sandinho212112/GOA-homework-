#printing numbers 1-10 using for loops
for i in range(11):
  print(1, 10)

#printing a random sentence
sentence = "this is my sentence"
for i in range(5):
    print(sentence)

#printing numbers 1-5 using whileloops.
i = 1
while i <= 5:
    print(i)
    i += 1

#printing hello 3 times using while loop
hello = 0
while hello <= 0:
  print("hello")
  hello = hello + 1

# user entering their age
age = input("enter ur age")

# age verification and printing of message before submission
if age > 0:
    print("ur age is positive.")
else:
    print("ur age is negative.")

# number check
number = input("enter number ")

# equals 10 to check and print the message before submission
if number == 10:
    print("number equals to 10")
else:
    print("number doesnt equal to 10")


# number check
number= input("enter number")


# check and print the message before entering
if number > 0 and number < 10:
    print("child")

# entering the three sides of the triangle into three variables
side1 = float(input("enter the first side of the triangle"))
side2 = float(input("enter the second side of the triangle"))
side3 = float(input("enter the third side of the triangle"))

# Checking the triangle assembly
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("its possible to assembly the triangle")
else:
    print("its not possible to assembly the triangle")

