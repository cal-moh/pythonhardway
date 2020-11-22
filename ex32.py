## A list is an ordered container of things. Lists are indiscriminate containers that can contain any type of objects in the same container. An array is an ordered vector, which can tontain only the same kinds of data types. Arrays have to be declared, lists don't. Lists can be added to, appended and so on. Lists can't deal with mathematical operations inside them. Lists can be looped straight off without explicit loop declaration. Finally, memory-wise, lists are more compute heavy, compared to arrays. 
# learning pop() and append() functions related to lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in the_count:
    print(f"This is count {number}")

#same as above
for fruit in fruits:
    print(f"A type of fruit:{fruit}")

# also notice we can go through mixed lists too
# notice we have to use {} since we don't know what's in it #Why's this a thing?
for i in change:
    print(f"I got {i}")
    
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# This next line doesn't work - which means that the append function is not an executing function, just a simple add-on sort of function
# elements.append(range(0,12,2))
for i in range(0,12,2):
    print(f"Adding {i} to the list.")
# append() is a function that lists understand
    elements.append(i)
#now we can print them out too
# if:
    # print("Jimbo")
for i in elements:
    print(f"Element was: {i}")