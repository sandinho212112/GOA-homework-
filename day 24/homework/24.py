def find_longest_word(words):
    longest_word = ""
    
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

words_list = ["apple", "banana", "strawberry", "kiwi"]
print(find_longest_word(words_list))  

#2
def transform_numbers(numbers):
    new_list = []
    
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num * num)
        else: 
            new_list.append(num + 2) 
    
    return new_list

numbers_list = [1, 2, 3, 4, 5]
print(transform_numbers(numbers_list))
