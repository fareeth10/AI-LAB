from collections import deque

def solve_water_jug(c1, c2, target):
queue = deque([((0, 0), [])])
visited = set()


while queue:
    (j1, j2), path = queue.popleft()

    if (j1, j2) in visited:
        continue
    visited.add((j1, j2))

    current_path = path + [(j1, j2)]

    if j1 == target or j2 == target:
        return current_path

    moves = [
        (c1, j2),
        (j1, c2),
        (0, j2),
        (j1, 0),
        (j1 - min(j1, c2 - j2), j2 + min(j1, c2 - j2)),
        (j1 + min(j2, c1 - j1), j2 - min(j2, c1 - j1))
    ]

    for state in moves:
        if state not in visited:
            queue.append((state, current_path))

return None
if name == "main":
c1, c2, target = 4, 3, 2
print(f"Solving Water Jug Problem for Jug 1 ({c1}L), Jug 2 ({c2}L), Target ({target}L)...\n")
solution = solve_water_jug(c1, c2, target)


if solution:
    print("Steps to achieve target:")
    for step, (j1, j2) in enumerate(solution):
        print(f"Step {step}: Jug 1 = {j1}L, Jug 2 = {j2}L")
else:
    print("No solution exists for the given capacities and target.")
