#1
def add(numbers):
    total_sum = 0
    for num in numbers:
        if num / 2 == int(num / 2):
            total_sum += num
    return total_sum

#2
def reverse_string(s):
    reversed_str = ""    
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i] 
    return reversed_str

#3
def factorial(n):
    
    if n == 0 or n == 1:
        return 1
  
    else:
        return n * factorial(n - 1)
    
#4
def common_elements(list1, list2):
    common = []  
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

#5
def count_vowels(s):
    vowels = 'aeiouAEIOU'  
    count = 0  
    for char in s:
        if char in vowels:  
            count += 1  
    return count

#6
def bubble_sort(lst):
    n = len(lst)  
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

#7
def are_permutations(s1, s2):
    if len(s1) != len(s2):
        return False

    char_count1 = {}
    char_count2 = {}

    for char in s1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1
    
    for char in s2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    return char_count1 == char_count2

#8
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

#9

def sort_by_length(strings):
    for i in range(1, len(strings)):
        key = strings[i]
        key_length = len(key)
        j = i - 1
 
        while j >= 0 and len(strings[j]) > key_length:
            strings[j + 1] = strings[j]
            j -= 1
 
        strings[j + 1] = key
    
    return strings
