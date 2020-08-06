import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
words_following_words = {}
split_words = words.replace("\n", " ").split(" ")
for i in range(0, len(split_words) - 1):
    if split_words[i] in words_following_words:
        words_following_words[split_words[i]].append(split_words[i + 1])
    else:
        words_following_words[split_words[i]] = [split_words[i + 1]]


# TODO: construct 5 random sentences
words_keys = words_following_words.keys()
stop_words = [word for word in words_keys if len(word) > 0 and ((word[len(word) - 1] == '"' and (word[len(word) - 2] == "." or word[len(word) - 2] == "?" or word[len(word) - 2] == "!")) or (word[len(word) - 1] == '\'' and word[len(
    word) - 2] == '\"' and (word[len(word) - 3] == '.' or word[len(word) - 3] == "?" or word[len(word) - 3] == "!")) or word[len(word) - 1] == "." or word[len(word) - 1] == "?" or word[len(word) - 1] == "!")]
start_words = [word for word in words_keys if len(word) > 0 and (
    word[0].isupper() or (word[0] == '"' and word[1].isupper())) and word not in stop_words]
start_word = random.choice(start_words)

key = start_word
stopped = False
for i in range(6):
    sentence = start_word
    while not stopped:
        next_word = random.choice(words_following_words[key])
        if next_word not in start_words:
            sentence += " " + next_word
            
        if next_word in stop_words:
            stopped = True
        key = next_word
    stopped = False
    print(sentence)
    start_word = random.choice(start_words)
