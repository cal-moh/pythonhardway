formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
# Also interesting that the next line writes True False, instead of a 1 0 or such boolean
print(formatter.format("True", False, 1, False))
# Didn't expect that the next line will have a curly braces only output. Should have expected this, missed it somehow. Interesting. Of course, I could keep using the format() function of the string array ad infinitum
# There's also an indent in the book at this point, of a single space. I think it's an error. A single space indent is an IndentationError
print(formatter.format(formatter, formatter, formatter, formatter))
# This is interesting - that you can break it out into multiple lines for readability, if you are careful to give it an indent.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
    ))