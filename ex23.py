## Trying to figure out what UTF 8 is. It's a popular encoding standard that dictates what a symbol means. ASCII holds a certain number of characters. UTF-8 is backward compatible for the first 128 characters, and has a different implementation for / and % from what I understand. Some other standards will exist for things like the Chinese language in writing - GB2312 standard, Big5 standard, Cyrllic for Russian (Windows-1251), Korean, Japanese and Hebrew, Marathi, Kannada, Pashto. Would be interesting to see if these break (UTF8 still pretty popular in these languages). A Unicode character is a code point - 1.1 million possible representations, but not all of them are used. Each such code point corresponds to a glyph - the character B is characterised by one vertical ink mark, and two semi-circles stacked on top of each other. And so on. https://docs.python.org/3/howto/unicode.html. Also trying to figure out what exactly is a code point - I think I need to spend some ten minutes on this - https://en.wikipedia.org/wiki/Code_point
# Why did the code not write "from sys import argv". Checked a little - argv is one file I think, which is better than importing the entire sys package
# Aliasing of packaging works
## Eval is clearly a dangerous function. What I attempted to do in this file - I attempted to write bytes to the file, and then read these back in 'b' mode, while I also attempted to write strings to the file, and read these back in strings mode. Unfortunately, I could not reproduce the exact hexadecimal representations in the execution. However, it looks like whenever the script puts out something like b'....', it's referring to the fact that this is a byte that's being printed, while a straight .... print is a string being printed. I guess I'll content myself with this and move on from this exercise. Update - I think I was done with this - here's stuff from Zed - https://forum.learncodethehardway.com/t/solved-lpthw3-exercise-23-extra-credit-3-reverse-script/71/10
from sys import argv as s
import ast
script, f, encoding, error = s

# Interesting that they are able to define a function called main. I think the problem comes in when the __main__ function is used/defined. 
def main(language_file, encoding, errors):
# This will read the line into the variable line, as a string
    line = language_file.readline().strip()
    # print(line)
# if line exists, print the line, its encoding, and its errors (whatever errors means)    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


# def print_line(line, encoding, errors): # A
    # next_lang = line.strip()
# ## Returns an encoded version of the string, (and is a string function), as set by encoding - https://www.tutorialspoint.com/python3/string_encode.htm
    # raw_bytes = next_lang.encode(encoding, errors=errors)
    # cooked_string = raw_bytes.decode(encoding, errors=errors)
    # print(raw_bytes, "<===>", cooked_string)

def print_line(line, encoding, errors): # B
    # next_lang = line.strip()
## Returns an encoded version of the string, (and is a string function), as set by encoding - https://www.tutorialspoint.com/python3/string_encode.htm
    # raw_bytes = next_lang.decode(encoding, errors=errors)
    raw_bytes = line.decode(encoding, errors=errors)
    cooked_string = raw_bytes.encode(encoding, errors=errors)
    print(raw_bytes, "<===>", cooked_string)
    # print(eval(line))
    # print(ast.literal_eval(line))
    
# languages = open(f, encoding="utf-8") # A
languages = open(f, "r+b") # B
# print(languages)

main(languages, encoding, error)