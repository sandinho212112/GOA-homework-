num = 5

print("----------- AND -----------")

print(num >= 1 and num <= 10) # True
print(num >= 1 and num <= 4) # False
print(num > 5 and num <= 10) # False
print(num > 5 and num > 10) # False

print("----------- OR -----------")

print(num >= 1 or num <= 10) # True
print(num >= 1 or num <= 4) # True
print(num > 5 or num <= 10) # True
print(num > 5 or num > 10) # False
# "and"ოპერატორი აჩვენებს True-ს თუ ორივე პირობა მის მარცხენა და მარჯვენა მხარეს არის True.თუ რომელიმე პირობა არის False ის აჩვენებს False-ს
# "or"ოპერატორი აჩვენებს True-ს თუ მის მარცხენა ან მარჯვენა მხარეს ერთ-ერთი პირობა მაინც არის True. თუ ორივე პირობა არის False ის აჩვენებს False-ს

#example 1
a = 10
b = 20
result = (a < b) and (a + b == 30)
print(result)  # True

#example 2
a = 15
b = 5
result = (a > b) and (a == b)
print(result)  # False

#example 3
a = 7
b = 14
result = (a > b) and (a * b < 50)
print(result)  # False

#example 4
a = 8
b = 8
result = (a == b) or (a > b)
print(result)  # True

#example 5
a = 3
b = 4
result = (a < b) or (a + b > 5)
print(result)  # True

#equal
a = 5
b = 5
result = (a == b)
print(result)  # True

#not equal
a = 5
b = 10
result = (a != b)
print(result)  # True

# is less
a = 3
b = 7
result = (a < b)
print(result)  # True

#is more
a = 10
b = 6
result = (a > b)
print(result)  # True

#is less than or equal to
a = 4
b = 4
result = (a <= b)
print(result)  # True

#is more than or equal to
a = 8
b = 8
result = (a >= b)
print(result)  # True


