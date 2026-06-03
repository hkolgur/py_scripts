"""find longest word that is present in a file"""

import json

with open("input_file.txt", "r") as file:
    content = file.read()
    split_content = content.split(" ")
    print(f"split content:{split_content}")
    split_content.sort(key=len, reverse=True)
    print(f"Largetst word in file is:{split_content[0]}")
    # print(content.split("\n").sort(key=len,reverse=True))
    # print(longest_word)

# Write split words to new file .'w' will overwrite an existing file,
# while 'x' will raise an error to prevent accidental data loss.
with open("split_words.txt", "w") as fp:
    for item in split_content:
        fp.write(item + " ")  # fp.write(item+"\n")
    fp.write("\n")
    
data = {"name": "Alice", "age": 30, "city": "New York"}

# Reopen the file and write JSON content.
#'x' will raise an error if file already exists
try:
    with open("split_words.txt", "x") as fp:
        json.dump(data,fp,indent=2)
except FileExistsError:
    with open("split_words.txt", "a") as fp:
        print("*****from Exception block******")
        json.dump(data,fp,indent=4)

# read back the file that is written and log data
with open("split_words.txt", "r") as fp:
    content = fp.read()
    print("From written file: ", content)
