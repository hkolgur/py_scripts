"""convert upper case to lower case"""

my_str = "My name is Hari"

new_str = ""
for ch in my_str:
    if ch.isalpha():
        new_str += ch.upper()
    else:
        new_str += ch

print(new_str)
