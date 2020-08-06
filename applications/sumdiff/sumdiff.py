"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

lookup = {}

def f(x):
    return x * 4 + 6

def sum(a, b):
    return f(a) + f(b)

def diff(c, d):
    return f(c) - f(d)

for i in range(len(q)):
    for j in range(len(q)):
        lookup[f"f({i}) + f({j})"] = sum(i, j)
        lookup[f"f({i}) - f({j})"] = diff(i, j)

print(sorted(lookup.items(), key=lambda x: x[1], reverse=True))