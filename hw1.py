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

def add_prices (dollars: int, cents: int)-> float: # takes in two integers representing dollars and cents and returns
    # a concatenated price as a float
    finalPrice = 0
    totalCents = 0
    if cents < 100:
        finalPrice = dollars + cents/100
    else:
        dollars = dollars / 100
        totalCents = dollars + cents/100
        finalPrice = totalCents / 100
    return finalPrice

# Part 5

def rectangle_area(top_left: list, bottom_right: list) -> int: # takes in a rectangle consisting of two Points and
    # returns the area as an int
    xRec = bottom_right[0] - top_left[0]
    yRec = top_left[1] - bottom_right[1]
    area = xRec * yRec
    return area

# Part 6

def books_by_author (author:str, books:list[data.Book])->list[data.Book]: # takes in a target author and a list of
    # books and returns book titles that are only by the target author
    filteredBooks = []
    for i in range(len(books)):
        for i in books.authors:
            if i == author:
                filteredBooks.append(books[i].title)

    return filteredBooks




# Part 7

def circle_bound(rect:data.Rectangle) -> data.Circle: # takes in a rectangle in two Points and returns a circle as a
    # radius and center point
    boundingCircle = data.Circle((0,0),0.0)
    rad = data.Circle.radius(0.0)
    cntrPt = data.Circle.center(0,0)
    xRec = data.Rectangle.bottom_right.x - data.Rectangle.top_left.x
    yRec = data.Rectangle.top_left.y - data.Rectangle.bottom_right.y
    if xRec > yRec:
        rad = data.Circle.radius(float(xRec))
    else:
        rad = data.Circle.radius(float(yRec))
    cntrPt = data.Circle.center(.5*xRec,.5*yRec)
    boundingCircle = data.Circle(cntrPt,rad)
    return boundingCircle



# Part 8

def below_pay_average(list:list[data.Employee]) -> list[str]: # takes in a list of employee names and their salaries
    # and returns a list of employees who are paid less than the average of all employee pay rates
    avrgPay = 0
    names = []
    for i in range(len(list)):
        avrgPay = avrgPay + i.Employee.pay_rate
    avrgPay = avrgPay / len(list)
    for i in list:
        if data.Employee.pay_rate < avrgPay:
            names.append(i.Employee.name)
    return names
