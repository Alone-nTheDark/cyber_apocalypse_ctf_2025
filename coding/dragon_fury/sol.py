# Input the text as a single string
input_text = input()  # Example: "shock;979;23"

# Write your solution below and make sure to encode the word correctly
target = int(input())

def find_combination(damage_options, target, index=0, current_combination=[]):
    if index == len(damage_options):
        if sum(current_combination) == target:
            return current_combination
        return None
    
    for value in damage_options[index]:
        result = find_combination(damage_options, target, index + 1, current_combination + [value])
        if result:
            return result
import ast

comb = eval(input_text.strip())
res = find_combination(comb, target)

print(res)

