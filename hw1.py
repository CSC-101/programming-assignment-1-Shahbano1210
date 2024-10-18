import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count (word:str)-> int: # takes in a word or words as str and returns the number of vowels in the word(s) as an int
    charList = list(word)
    vowels = ["a","A","e", "E", "I","i","O","o","U","u"]
    count = 0
    for i in vowels:
        if i in charList:
            count = count +1
    return(count)


# Part 2

def short_lists(input_list:list[list[int]]) -> list: # takes in a list of nested lists of int and returns a new list
    # of only the nested lists of length 2
    newList = []
    for i in range(len(input_list)):
        if len(input_list[i]) == 2:
            newList.append(input_list[i])
    return newList


# Part 3

def ascending_pairs (input_list:list[list[int]]) -> list: # takes in a list of nested lists of int and returns the same
    # list but any nested lists of length 2 are arranged in ascending order
    newList = []
    for i in range(len(input_list)):
        if len(input_list[i]) == 2 and input_list[i][0] > input_list[i][1]:
            x = input_list[i][0]
            y = input_list[i][1]
            input_list[i][0] = y
            input_list[i][1] = x
        newList.append(input_list[i])
    return newList

# Part 4


# Part 5


# Part 6


# Part 7


# Part 8


