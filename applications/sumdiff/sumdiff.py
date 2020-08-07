"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

sum_lookup = {}
diff_lookup = {}

def f(x):
    return x * 4 + 6

def sum(a, b):
    return f(a) + f(b)

def diff(c, d):
    return f(c) - f(d)

for i in range(len(q)):
    for j in range(len(q)):
        f_i = f(q[i])
        f_j = f(q[j])
        if f"f({q[i]}) + f({q[j]})" not in sum_lookup:
            sum_lookup[f"f({q[i]}) + f({q[j]})"] = (f_i, f_j, f_i + f_j)
        if f"f({q[i]}) - f({q[j]})" not in diff_lookup:
            diff_lookup[f"f({q[i]}) - f({q[j]})"] = (f_i, f_j, f_i - f_j)
        if f"f({q[j]}) - f({q[i]})" not in diff_lookup:
            diff_lookup[f"f({q[j]}) - f({q[i]})"] = (f_j, f_i, f_j - f_i)

for sum_item in sum_lookup.items():
    for diff_item in diff_lookup.items():
        if sum_item[1][2] == diff_item[1][2]:
            print(f"{sum_item[0]} = {diff_item[0]}    {sum_item[1][0]} + {sum_item[1][1]} = {diff_item[1][0]} - {diff_item[1][1]}")

