from utils import (
    reverse_string, count_vowels,
    add, sub, multi, div,
    write_file, read_file, append_file,
    reverse_text, count_words, to_upper
)

# Make a module for string functions

print(reverse_string("helloimran"))
print(count_vowels("Imransayyad"))

# Make a module for math functions

"""
Create a package called utils
    Add:
        utils/file_utils.py
        utils/text_utils.py
Import both modules in main file and use them  """


# File functions
print(write_file("sample.txt", "Hello Imran"))
print(append_file("sample.txt", "\nWelcome to utils package"))
print(read_file("sample.txt"))

# Text functions
text = "hello world from utils"
print(reverse_text(text))
print(count_words(text))
print(to_upper(text))


