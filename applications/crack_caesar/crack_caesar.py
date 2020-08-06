# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

key = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# open and read contents of ciphertext.txt
with open("ciphertext.txt") as f:
    text = f.read()

# use hash table to keep track character count

# loop through characters
# for sentence in text:
count_chars = {}
for char in text:
## if key is found
    if char in count_chars:
##   add 1 to value of key
        count_chars[char] += 1
## else
    elif char.isalpha() and char not in count_chars:
##   assign 1 to key
        count_chars[char] = 1

# sort counted chars by frequency. most frequent being at the top, and least frequent being at the bottom
ordered_count = [char[0] for char in sorted(count_chars.items(), key=lambda x: x[1], reverse=True)]

# convert text string into an array of chars
text_chars = list(text)
# pre-allocate same number of slots for the decoded string as the number of characters from the original text
decoded_str = [None] * len(text_chars)

for i in range(len(ordered_count) - 1):
    for j in range(len(text_chars)):
        if text_chars[j] == ordered_count[i]:
            decoded_str[j] = key[i]
        elif decoded_str[j] is None:
            decoded_str[j] = text_chars[j]

print("".join(decoded_str))

    


