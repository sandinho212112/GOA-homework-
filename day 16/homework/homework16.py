#pop

#1
numbers = [1,2,3,4,5]
numbers.pop(4)
numbers.append(5)
print(numbers)

#2
cars = ["mersedes","pagani","ferrari","toyota","bmw"]
cars.pop(0)
cars.append("mercedes")
print(cars)

#3
char_list=["a","b","c","d","e"]
char_list.pop(2)
print(char_list)

#4
char_list=["a","b","c","d","e"]
char_list.pop(4)
char_list.append("e")
print(char_list)

#count
#1
ints=[1,2,3,4,5,6,7,8,9]
print(ints.count(5))

#2
strings=["avocado","banana","mango","pineapple"]
count_a = sum(a.count("a") for a in strings)
print(count_a)

#3 
bool=[True,False,True,False,True,True,False]
count_true=bool.count(True)
print(count_true)

#len

#1
ints=[1,2,3,69,22,551,90,82,1000,21]
print(len(ints))

#2
week_days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print(len(week_days))

#3
nested_list = [
    [1, 2, 3],  
    [4, 5, 6],        
    [7, 8, 9]        
]
print(len(nested_list))