""" find lenght of last word in a sentence"""

my_str=" hello my hobbies are playing @CAricket"

print(len(my_str.strip(" ").split(" ")[-1]))