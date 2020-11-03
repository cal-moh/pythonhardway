tabby_cat = "\tI'm \vtabbed in."
# \n goes to next line. \t tabs something in 
persian_cat = "I'm split\non a line."
# backslash can suppress itself too
# Interesting - what does a \a do? It's making the "a" disappear right now. \b made the space disappear too! \c and \d appear as "\c" and "\d"
# So \a is a bell character. Apparently, this whole thing can sometimes read this and make a bell sound
backslash_cat = "I'm -\a a cat."

# Interestingly, can't interrupt a """ line with a comment
fat_cat = '''
 I'll do a list:
\v\* Cat food
\t\* Fishies
\t\* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)