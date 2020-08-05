def word_count(s):
    chars_to_remove = set(['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&'])
    count = {}
    s = ' '.join(s.split())
    s = ''.join([c for c in s if c not in chars_to_remove]).lower()
    if s == '':
        return {}
    words = s.split(" ")
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

if __name__ == "__main__":
    sorted_word_count = sorted(word_count(''.join(open("robin.txt"))).items(), key=lambda x: x[1], reverse=True)
    for word in sorted_word_count:
        print(word[0] + ' '*(17 - len(word[0])) + '#'*word[1])