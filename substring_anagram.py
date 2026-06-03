"""check if a given substring is present as anagram in a given string.
Return starting and ending index locations of the match found.
Anagram means letters of word can be in any order but has to match exact count"""

from collections import Counter
# eer -> herr

source_str = "greyhounohyd"
target_str = "yoh"
source_len = len(source_str)
k = len(target_str)

target_counter = Counter(target_str)
result = []
if source_len >= k:
    current_counter = Counter(source_str[:k])
    if current_counter == target_counter:
        # result.append(current_counter.copy())
        result.append([0, k - 1])
    for i in range(source_len - k):
        char_leaving = source_str[i]
        current_counter[char_leaving] -= 1
        if current_counter[char_leaving] == 0:
            del current_counter[char_leaving]

        char_entering = source_str[i + k]
        current_counter[char_entering] += 1
        if current_counter == target_counter:
            # result.append(current_counter.copy())
            result.append([i + 1, i + k])
            # print(f"R curr_ctr:{current_counter},{target_counter} result:{result}")
    print("\n Matching starting and ending index positions:", result)

else:
    print("Source string is smaller than target substring")
