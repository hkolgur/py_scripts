"""Reverse words in a given string if the string contains more than one word
else if string has one word, then return same word"""


# IMP: strings are immutable so no reverse in built function.
# str[::-1]->gives string in reverse order
def reverse_words(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    if len(s.split()) > 1:
        return " ".join(s.split()[::-1])  # join splitted words to form the string
    else:
        return s


my_str = "My name is Hari"
my_word = "Hari"

print("Original String:", my_str)
print("Reversed String:", reverse_words(my_str))
print("Original word:", my_word)
print("Reversed word:", reverse_words(my_word))
