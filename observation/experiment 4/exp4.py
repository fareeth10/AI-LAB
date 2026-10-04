from itertools import permutations

def solve_cryptarithmetic(w1, w2, w3):
unique_letters = list(set(w1 + w2 + w3))
if len(unique_letters) > 10:
return None


first_letters = {w1[0], w2[0], w3[0]}

for perm in permutations(range(10), len(unique_letters)):
    mapping = dict(zip(unique_letters, perm))

    if any(mapping[char] == 0 for char in first_letters):
        continue

    num1 = int("".join(str(mapping[c]) for c in w1))
    num2 = int("".join(str(mapping[c]) for c in w2))
    num3 = int("".join(str(mapping[c]) for c in w3))

    if num1 + num2 == num3:
        return mapping, num1, num2, num3

return None
if name == "main":
w1, w2, w3 = "SEND", "MORE", "MONEY"
print(f"Solving Cryptarithmetic Problem: {w1} + {w2} = {w3}\n")
result = solve_cryptarithmetic(w1, w2, w3)


if result:
    mapping, n1, n2, n3 = result
    print("Letter Mapping:")
    for char, digit in sorted(mapping.items()):
        print(f"{char} = {digit}")
    print(f"\nEquation Solution:\n  {n1}\n+ {n2}\n------\n  {n3}")
else:
    print("No solution exists.")
