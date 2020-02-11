"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import sys

with open(sys.path[0] + '\\foo.txt') as f:
    print(f.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

lines = ['Spock wants to go swim\n', 'Why are all the pools empty?\n', 'No rain on Vulcan']
with open(sys.path[0] + '\\bar.txt', 'w') as f:
    for line in lines:
        f.writelines(line)

with open(sys.path[0] + '\\bar.txt') as f:
    for i, line in enumerate(f):
        if lines[i] == line:
            print(line, end='')
        else:
            print("Comparison failed!")
