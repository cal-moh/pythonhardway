# The purpose of this exercise is to get hands set on the print function
print("Mary had a little lamb")
# The next line is interesting - instead of naming a string variable and accessing its format() function, we used the string directly, on the fly, and utilised its format() function
print("It's fleece was white as {}".format('sheet metal'))
print("And everywhere that Mary went")
print("." * 10)  #wonder what this would do. Interesting - this leads to ten dots

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#Watch that comma at the end. try removing it to see what happens
# The comma makes the variable name invalid. The null printed at the end is interesting - it suppresses the \n character
print(end1 + end2 + end3 + end4 + end5 + end6, end='')
print(end7 + end8 + end9 + end10 + end11 + end12)