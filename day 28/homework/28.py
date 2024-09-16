#1 volume of cuboid

def calculate_volume(length, width, height):
    volume = length * width * height
    return volume

#2 Price of Mangoes

def mango(quantity, price_per_mango):
    # Calculate the number of groups of 3
    groups_of_3 = quantity // 3
    
    # group mangoebi
    mangoes_paid_in_groups = groups_of_3 * 2
    
    # leftover mangoebi
    leftover_mangoes = quantity % 3
    
    # mangoebi jami
    total_mangoes_to_pay_for = mangoes_paid_in_groups + leftover_mangoes
    
    # jami
    total_cost = total_mangoes_to_pay_for * price_per_mango
    
    return total_cost

#3 reversed words
def reverse_words(sentence):
    # Step 1: Split the sentence into words
    words = sentence.split()
    
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]
    
    # Step 3: Join the reversed list back into a single string
    reversed_sentence = " ".join(reversed_words)
    
    return reversed_sentence
