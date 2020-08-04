def no_dups(s):
    dups = {}
    words = s.split(" ")
    new_s = []
    for word in words:
        if word not in dups:
            dups[word] = 1
            new_s.append(word)
    new_s = ' '.join(new_s)
    return new_s



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))