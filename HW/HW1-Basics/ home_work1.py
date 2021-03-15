import matplotlib.pyplot as plt
from collections import Counter
import itertools
from itertools import *
import numpy as np
import string
import seaborn as sns

# List - It is a data structure/ data type that is ordered and that order will not change. It is changeable meaning
# that we can add and remove items in a list after it is created.
# append - To add an item to the end of the list.
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# extend - To append elements from another list to the current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# index - List items are indexed and you can access them by referring to the index number
# The index() method returns the index of the given element in the list. The index() method only returns the
# first occurrence of the matching element. If the element is not found, a ValueError exception is raised.
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
print('The index of banana:', thislist.index("banana"))

# index(value, integer)  - 'i' after the 4th index is searched
alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
index = alphabets.index('i', 4)
print('The index of i:', index)

# insert(position) - To insert a list item at a specified index position.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# remove() - To removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# pop() - To removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# count() - Returns the number of times the value appears in the list
thislist = ["banana", "Orange", "cherry", "Kiwi", "cherry"]
count = thislist.count("cherry")
print(count)

# reverse() - Reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# sort() - To sort the list alphanumerically, ascending, by default.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist.sort(reverse=True)
print(thislist)

# [1]+[1] produces [1, 1]
# [2]*2 produces [2, 2]
# [1,2][1:] produces [2]
# [x for x in [2,3]] produces [2, 3]
# [x for x in [1,2] if x ==1] produces [1]
# [y*2 for x in [[1,2],[3,4]] for y in x] produces [2, 4, 6, 8]

# Tuple - It is a collection which is ordered and unchangeable. Tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# count() - Return the number of times the value appears
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# index() - Searches the tuple for a specified value and returns the position of where it was found
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

# build a dictionary from tuples
t = ((1, 'a'), (2, 'b'))
dict((y, x) for x, y in t)

# unpack tuples - When we create a tuple, we normally assign values to it. This is called packing a tuple.
# But, in Python, we are also allowed to extract the values back into variables. This is called unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Dictionary - Used to store data values in key:value pairs. It is a collection which is unordered, changeable and
#  does not allow duplicates. Dictionaries are written with curly brackets, and have keys and values
a_dict = {'I hate': 'you', 'You should': 'leave'}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# keys() - It will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)

# items() - It will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
print(x)

# hasvalues() - Not sure, dictionary has a method values() which lists all the values available in a given dictionary
x = thisdict.values()
print(x)

# key() - Not sure, dictionary has method has_key() was removed in Python3. in method is used to check if key exists
x = "brand" in thisdict
print(x)

# ‘never’ in a_dict -> produces false. It basically checks if never is a key in the dictionary.
# del a_dict['me'] -> del method deletes the key from the dict. In this case 'me' is not a key and hence raise KeyError.
# a_dict.clear() -> removes all the elements from the dictionary.

# sets - is a collection which is unordered and unindexed. No duplicate members. Sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)

# add() - To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# remove() - To remove an item in a set, use the remove(), or the discard() method.
# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
thisset.discard("orange")
print(thisset)

# pop() - You can also use the pop(), method to remove an item, but this method will remove the last item.
# sets are unordered, so you will not know what item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# clear() - The clear() method empties the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Strings - Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# len() - The len() function returns the length of a string
a = "Hello, World!"
print(len(a))

# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

# The upper() method returns the string in upper case and lower() in lower case
a = "Hello, World!"
print(a.upper())
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method returns a list where the text between the specified separator becomes the list items
a = "Hello, World!"
print(a.split(","))

# Counter - It is a subclass of the dict class. It keeps track of the frequency of each element in the container.
my_count = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print(my_count)
my_count = Counter("Hello World")
print(my_count)
my_count = Counter({'a': 3, 'b': 2, 'c': 1})
print(my_count)
# most_common() - retrieves the highest frequency values
my_count.most_common()

# Python’s Itertool is a module that provides various functions that work on iterators to produce complex iterators
# Permutations() - generate all possible permutations of an iterable.
print(list(permutations([1, 'geeks'], 2)))

# Combinations() - This iterator prints all the possible combinations(without replacement) 
print(list(combinations(['A', 2], 2)))  

# count(start, step) - This iterator starts printing from the “start” number and prints infinitely
for i in count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")

# repeat(val, num)- This iterator repeatedly prints the passed value infinite number of times
print("Printing the numbers repeatedly : ")   
print(list(itertools.repeat(25, 4)))

########################################################################################################################

flower_orders = ['W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B',
                 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B',
                 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R/B', 'W/R', 'W/R', 'W/R', 'W/R',
                 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'W/R', 'R/V/Y', 'R/V/Y',
                 'R/V/Y', 'R/V/Y', 'R/V/Y', 'R/V/Y', 'R/V/Y', 'R/V/Y', 'R/V/Y', 'R/V/Y', 'W/R/V', 'W/R/V', 'W/R/V',
                 'W/R/V', 'W/R/V', 'W/R/V', 'W/R/V', 'W/R/V', 'W/R/V', 'W/R/V', 'W/N/R/V', 'W/N/R/V', 'W/N/R/V',
                 'W/N/R/V', 'W/N/R/V', 'W/N/R/V', 'W/N/R/V', 'W/N/R/V', 'W/R/B/Y', 'W/R/B/Y', 'W/R/B/Y', 'W/R/B/Y',
                 'W/R/B/Y', 'W/R/B/Y', 'B/Y', 'B/Y', 'B/Y', 'B/Y', 'B/Y', 'R/B/Y', 'R/B/Y', 'R/B/Y', 'R/B/Y', 'R/B/Y',
                 'W/N/R/B/V/Y', 'W/N/R/B/V/Y', 'W/N/R/B/V/Y', 'W/N/R/B/V/Y', 'W/N/R/B/V/Y', 'W/G', 'W/G', 'W/G', 'W/G',
                 'R/Y', 'R/Y', 'R/Y', 'R/Y', 'N/R/V/Y', 'N/R/V/Y', 'N/R/V/Y', 'N/R/V/Y', 'W/R/B/V', 'W/R/B/V',
                 'W/R/B/V', 'W/R/B/V', 'W/N/R/V/Y', 'W/N/R/V/Y', 'W/N/R/V/Y', 'W/N/R/V/Y', 'N/R/Y', 'N/R/Y',
                 'N/R/Y', 'W/V/O', 'W/V/O', 'W/V/O', 'W/N/R/Y', 'W/N/R/Y', 'W/N/R/Y', 'R/B/V/Y', 'R/B/V/Y',
                 'R/B/V/Y', 'W/R/V/Y', 'W/R/V/Y', 'W/R/V/Y', 'W/R/B/V/Y', 'W/R/B/V/Y', 'W/R/B/V/Y', 'W/N/R/B/Y',
                 'W/N/R/B/Y', 'W/N/R/B/Y', 'R/G', 'R/G', 'B/V/Y', 'B/V/Y', 'N/B/Y', 'N/B/Y', 'W/B/Y', 'W/B/Y',
                 'W/N/B', 'W/N/B', 'W/N/R', 'W/N/R', 'W/N/B/Y', 'W/N/B/Y', 'W/B/V/Y', 'W/B/V/Y', 'W/N/R/B/V/Y/G/M',
                 'W/N/R/B/V/Y/G/M', 'B/R', 'N/R', 'V/Y', 'V', 'N/R/V', 'N/V/Y', 'R/B/O', 'W/B/V', 'W/V/Y', 'W/N/R/B',
                 'W/N/R/O', 'W/N/R/G', 'W/N/V/Y', 'W/N/Y/M', 'N/R/B/Y', 'N/B/V/Y', 'R/V/Y/O', 'W/B/V/M', 'W/B/V/O',
                 'N/R/B/Y/M', 'N/R/V/O/M', 'W/N/R/Y/G', 'N/R/B/V/Y', 'W/R/B/V/Y/P', 'W/N/R/B/Y/G', 'W/N/R/B/V/O/M',
                 'W/N/R/B/V/Y/M', 'W/N/B/V/Y/G/M', 'W/N/B/V/V/Y/P']

# 1. Build a counter object and use the counter and confirm they have the same values.
flower_orders_cleaned = [x.replace('/', '') for x in flower_orders]
count_obj = dict([(x, flower_orders_cleaned.count(x)) for x in set(flower_orders_cleaned)])
counter_obj = Counter(flower_orders_cleaned)
groupby_obj = [(i, len(list(c))) for i, c in groupby(flower_orders_cleaned)]
print("The count object :" + str(count_obj))
print("The counter object :" + str(counter_obj))
print("The groupby object :" + str(groupby_obj))
print("Checking the difference :" + str(Counter(count_obj) - counter_obj))

# 2. Count how many objects have color W in them.
print("Number of objects having color W :" + str(len([color for color in flower_orders_cleaned if "W" in color])))

# 3. Make histogram of colors.
flower_colors = ''.join([elem for elem in flower_orders_cleaned])
colors_dict = dict(Counter(list(flower_colors)))
plt.bar(colors_dict.keys(), colors_dict.values())
plt.show()

# 4. Rank the pairs of colors in each order regardless of how many colors are in an order.
doubles = list()
for order in flower_orders:
    doubles += list(itertools.combinations(order.split('/'), 2))
double_counts = Counter(doubles)
print("The pairs of colors :")
print(double_counts.most_common())

# 5. Rank the triplets of colors in each order regardless of how many colors are in an order.
triples = list()
for order in flower_orders:
    triples += list(itertools.combinations(order.split('/'), 3))
print(triples)
triple_counts = Counter(triples)
print("The triplets of colors :")
print(triple_counts.most_common())

# 6. Make dictionary color for keys and values are what other colors it is ordered with.
all_colors = list(set([item for sublist in flower_orders for item in sublist.split('/')]))
dict_colors = {}
for color in all_colors:
    for order in list(set(flower_orders)):
        if color in order:
            colors = order.split('/')
            colors.remove(color)
            dict_colors[color] = colors
print("Dictionary of color with other colors :")
print(dict_colors)

# 7. Probability of having an edge between two colors based on how often they co-occur.
double_color_probability = {k: np.round(v / len(doubles), 2) for k, v in double_counts.items()}
print("Probability of having an edge between two colors :")
print(double_color_probability)

# 8. Make 10 business questions related to the questions we asked above.
# 1. The list could be a movie list where each element is a list of movies watched by users.
# 2. We can use this list to find the most watched movie or top 10 movies watched.
# 3. We can use above to find movies watched together (pairs) and triplets
# 4. We can use this as a recomendation engine to suggest other movies that can we watched based on the data.
# 5. We can also cluster users based on the movies watched.
# The same can be applied to products bought etc.


########################################################################################################################
dead_men_tell_taies = ['Four score and seven years ago our fathers brought forth on this',
                       'continent a new nation, conceived in liberty and dedicated to the',
                       'proposition that all men are created equal. Now we are engaged in',
                       'a great civil war, testing whether that nation or any nation so',
                       'conceived and so dedicated can long endure. We are met on a great',
                       'battlefield of that war. We have come to dedicate a portion of',
                       'that field as a final resting-place for those who here gave their',
                       'lives that that nation might live. It is altogether fitting and',
                       'proper that we should do this. But in a larger sense, we cannot',
                       'dedicate, we cannot consecrate, we cannot hallow this ground.',
                       'The brave men, living and dead who struggled here have consecrated',
                       'it far above our poor power to add or detract. The world will',
                       'little note nor long remember what we say here, but it can never',
                       'forget what they did here. It is for us the living rather to be',
                       'dedicated here to the unfinished work which they who fought here',
                       'have thus far so nobly advanced. It is rather for us to be here',
                       'dedicated to the great task remaining before us--that from these',
                       'honored dead we take increased devotion to that cause for which',
                       'they gave the last full measure of devotion--that we here highly',
                       'resolve that these dead shall not have died in vain, that this',
                       'nation under God shall have a new birth of freedom, and that',
                       'government of the people, by the people, for the people shall',
                       'not perish from the earth.']


# 1. Join everything
strings_joined = ' '.join(dead_men_tell_taies)
print("List with string objects joined :" + str(strings_joined))

# 2. Remove spaces
spaces_removed = strings_joined.replace(" ", "")
print("String with spaces removed :" + str(spaces_removed))

# 3. Occurrence probabilities for letters
letters = ''.join([i for i in spaces_removed if i.isalpha()]).casefold()
letters_count = dict(Counter(letters))
letters_proability = {k: np.round(v / len(letters), 2) for k, v in letters_count.items()}
print("Occurrence probabilities for letters : " + str(letters_proability))

# 4. Tell me transition probabilities for every letter pairs
string_list = list(letters)
letter_pairs = [(string_list[i], string_list[i + 1]) for i in range(0, len(string_list) - 1)]
letter_pairs_count = dict(Counter(letter_pairs))
letter_pairs_probability = {k: np.round(v / len(letter_pairs_count), 2) for k, v in letter_pairs_count.items()}
print("Transition probabilities for every letter pairs : " + str(letter_pairs_probability))

# 5. Make a 26x26 graph of 4. in numpy
for char in list(string.ascii_lowercase):
    letter_pairs_probability.setdefault((char, char), 0)
keys = sorted(set([y for x in list(dict(letter_pairs_probability).keys()) for y in x]))
np_matrix = np.zeros((26, 26))
for k, v in list(dict(letter_pairs_probability).items()):
    np_matrix[keys.index(k[0])][keys.index(k[1])] = np.round(v, 2)
print("26x26 graph")
print(np_matrix)

# 6. plot graph of transition probabilities from letter to letter - OPTIONAL
labels = list(string.ascii_lowercase)
ax = sns.heatmap(np_matrix, linewidth=0.3, xticklabels=labels, yticklabels=labels)
plt.show()

# 7. Flatten nested list - Unrelated


def flatten(input_list):
    rt = []
    for i in input_list:
        if isinstance(i, list):
            rt.extend(flatten(i))
        else:
            rt.append(i)
    return rt


list1 = ['image10', ['image00', 'image01'], ['image02', ['image03', 'image04']]]
list2 = flatten(list1)
print("Flattened nested list :" + str(list2))
