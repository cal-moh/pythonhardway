name = 'Zed A Shaw'
# Can't start a variable name with a number. Has to be a letter. Can't even be a special character
age = 35 # a total fabrication
height = 74 #inches
weight = 180 #lbs
# Attempting a space in the next variable assignment. Checked this - doesn't work. No spaces in variable names
# my _weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
# Attempted single quotes in the next line - doesn't work because of the apostrophe. Attempted a pair of double quotes in the middle, seems to be okay. Anything other than an operator between the middle quotes looks like it's going to throw up an error. 
# print("Actually that's not" != " too heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
# Interesting that a single formatting f took care of all variables inside
print(f"If I add {age}, {height}, and {weight}, I get {total}.")
#Wonder if I can do this. Clearly, this works too. Why'd I need to declare new variables then, when I can do this in the middle of a line? Readability versus memory efficiency?
print(f"The sum of {age}, {height}, {weight} = {age + height + weight}")
height_in_centimeters = round(height * 2.54, 1)
weight_in_kilograms = round(weight / 2.2, 1)
print(f"His measurements in the SI system - height {height_in_centimeters} cm, and weight {weight_in_kilograms} kg.")