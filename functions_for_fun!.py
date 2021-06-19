"""
HOW TO WRITE FUNCTIONS CORRECTLY?
# DRY (dont repeat yourself)
# DoT (Do one Thing)
# Modularity """

""" ## EXAMPLE: User-Interactive Alternate Function ## 
Creating a user-interactive alternate function that when a string is given by the user, 
it alternates, capitalizes the letters in even indexes and makes lower cases in odd indexes and 
consequently assigning to a new index.

for example: 
input: "data science"
output: DaTa sCiEnCe
"""


def alternating(string):
    new_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            new_string += string[i].upper()
        else:
            new_string += string[i].lower()
    print(new_string)


alternating(string=input("Please enter the string here!"))


# entered input => feature engineering
# OUTCOME : FeAtUrE EnGiNeErInG


# ==============================================

# Let's try generating a similar function with enumerate that does the same thing.

def alternate(string):
    new_string = ""
    for index, letter in enumerate(string):
        if index % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)


alternate(string=input("Please enter the string here!"))

# entered input => exploratory data analysis
# OUTPUT => ExPlOrAtOrY DaTa aNaLySiS


# ==============================================
# ==============================================

""" ## EXAMPLE : Function that groups numbers according to even-odd and odd-even indexes ## 

Randomly generated 30 numbers will be grouped according to their even-odd feature and even-odd indexes and 
will be placed on a new list that has 4 sub-list!  [[], [], [], []]

for example: 
[] => even numbers in even indexes
[] => odd numbers in odd indexes
[] => odd numbers in even indexes
[] => even numbers in odd indexes
"""

import numpy as np

numbers = np.random.randint(30, size=30)
numbers
# array([23,  1,  8,  2,  3,  8,  7, 21, 21,  0, 25, 21, 19,  4, 11, 22, 27, 2, 14,  4, 29, 16, 23,  4,  3, 26,  6, 27,  9, 18])


def even_odd_num():
    new_list = [[], [], [], []]
    for i, num in enumerate(numbers):
        if i % 2 == 0 and num % 2 == 0:  # even numbers in even indexes
            new_list[0].append([num, i])

        elif i % 2 != 0 and num % 2 != 0:  # odd numbers in odd indexes
            new_list[1].append([num, i])

        elif i % 2 == 0 and num % 2 != 0:  # odd numbers in even indexes
            new_list[2].append([num, i])

        else:  # even numbers in odd indexes
            new_list[3].append([num, i])
    print(new_list)


even_odd_num()

# [[[8, 2], [14, 18], [6, 26]],                                                                                                # new_list[0]
# [[1, 1], [21, 7], [21, 11], [27, 27]],                                                                                       # new_list[1]
# [[23, 0], [3, 4], [7, 6], [21, 8], [25, 10], [19, 12], [11, 14], [27, 16], [29, 20], [23, 22], [3, 24], [9, 28]],            # new_list[2]
# [[2, 3], [8, 5], [0, 9], [4, 13], [22, 15], [2, 17], [4, 19], [16, 21], [4, 23], [26, 25], [18, 29]]]                        # new_list[3]

# ==============================================
# ==============================================


""" ## EXAMPLE: Function that divides students into groups based on the first case letter of their names 
and placing to the sub-lists according to their alphabetic sequence ##
"""

students = ["John", "Mark", "Alison", "Jessica", "Alice", "Vanessa", "Mariam", "Michael", "Jennifer", "Victor"]


def divide(students):
    sub_lists = [[], [], [], []]

    for i in range(len(students)):
        if students[i].startswith("A"):
            sub_lists[0].append(students[i])
        elif students[i].startswith("J"):
            sub_lists[1].append(students[i])
        elif students[i].startswith("M"):
            sub_lists[2].append(students[i])
        else:
            sub_lists[3].append(students[i])

    print(sub_lists)


divide(students)

# [['Alison', 'Alice'], ['John', 'Jessica', 'Jennifer'], ['Mark', 'Mariam', 'Michael'], ['Vanessa', 'Victor']]


# ==============================================
# ==============================================

""" ## EXAMPLE: Function that divides people into groups based on their index number and placing to the sub-lists ##
"""

people = ["John", "Mark", "Alison", "Jessica", "Alice", "Vanessa", "Mariam", "Michael", "Jennifer", "Victor"]


def divide_func(people):
    groups = [[], []]
    for index, person in enumerate(people):
        if index % 2 == 0:
            groups[0].append(person)
        else:
            groups[1].append(person)
    print(groups)


divide_func(people)

# [['John', 'Alison', 'Alice', 'Mariam', 'Jennifer'], ['Mark', 'Jessica', 'Vanessa', 'Michael', 'Victor']]


# ==============================================
# ==============================================

""" ## EXAMPLE: # define a function that deletes strings iteratively as the first step and 
prints out the first version of the list without strings,
 then rounds the remaining floats and prints out: Last version of the list, floats rounded: ##
"""

bunch = [11, 22, 33, 44, 55, "a", "b", "c", 99.9, 88.8, 77.7, 66.6]


def laminar_func(any_list):
    for i in list(any_list):
        if type(i) == str:
            any_list.pop(any_list.index(i))
    print(f"First version of the list without strings:, {any_list}")

    for i in range(len(any_list)):
        if type(any_list[i]) == float:
            any_list[i] = round(any_list[i])

    print(f"Last version of the list, floats rounded:, {any_list}")


laminar_func(bunch)

# First version of the list without strings: [11, 22, 33, 44, 55, 99.9, 88.8, 77.7, 66.6]
# Last version of the list, floats rounded: [11, 22, 33, 44, 55, 100, 89, 78, 67]


""" ## EXAMPLE: # define a function named standart_scaler that standardizes the Age variable in titanic dataset##
"""

import pandas as pd


def load_titanic():
    data = pd.read_csv("Datasets/titanic.csv")
    return data


df = load_titanic()

df["Age"].head()


# Out[12]:
# 0    22.0
# 1    38.0
# 2    26.0
# 3    35.0
# 4    35.0


def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()


df[["Age"]].apply(standart_scaler).head()

#         Age
# 0 -0.530005
# 1  0.571430
# 2 -0.254646
# 3  0.364911
# 4  0.364911


# with lambda , without using defined function
df.loc[:, df.columns.str.contains("Age")].apply(lambda x: (x - x.mean()) / x.std())


