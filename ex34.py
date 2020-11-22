## Ordinal numbers since it indicates ordering of some kind. An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th etc. Most ordinal numbers end in "th" except for: one ⇒ first (1st) two ⇒ second (2nd) three ⇒ third (3rd). Cardinal numbers, the kinds used for indexing in programming, can be thought of as ordinal minus one. 1st element is element[0], and so on. 

animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

def ordinal_cardinal(i, j, k):
    ###i is the ordinal input, j is the cardinal input
    print(f"The animal at position {i} is {k[j]}")

ordinal_cardinal(2, 1, animals)
ordinal_cardinal(3, 2, animals)
ordinal_cardinal(1, 0, animals)
ordinal_cardinal(4, 3, animals)
ordinal_cardinal(5, 4, animals)
ordinal_cardinal(3, 2, animals)
ordinal_cardinal(6, 5, animals)
ordinal_cardinal(5, 4, animals) 


food_items = ['bun maska', 'bun bhujia', 'bun omelette', 'bun samosa', 'vada pav']

print(f"The fifth item in this list is {food_items[4]}")
print(f"The item with cardinal index 2 is {food_items[2]}")
print(f"The first item in this sequence is {food_items[0]}")
