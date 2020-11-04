from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

open(argv[2], 'w').write(open(argv[1], 'r').read())

# print(f"Copying from {from_file} to {to_file}")

# # we could do these two on one line, how?
# # I want to write this next line as:
# # with open(from_file, 'r') as in_file: # A -- uncomment for A
  # # indata = in_file.read() # A -- uncomment for A

# # I'm curious if this closes a file as well
# indata = open(from_file).read() # B -- uncomment for B

# # in_file = open(from_file) # B -- comment for A, B
# # indata = in_file.read() # B -- comment for A, B

# print(f"The input file is {len(indata)} bytes long")
# # Interesting that exists() is a function associated with the file stream object
# print(f"Does the output file exist?{exists(to_file)}")
# print("Read, hit RETURN to continue, CTRL-C to abort.")
# input()

# # I want to write this next line as:
# # with open(to_file, 'w') as out_file:
# #   out_file.write(indata)

# out_file = open(to_file, 'w')
# out_file.write(indata)

# print("Alright, all done.")

# # out_file.close() # A -- comment for A
# # from_file.close() # A -- comment for A