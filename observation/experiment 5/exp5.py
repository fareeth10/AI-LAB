from collections import deque

def is_safe(m, c):
if m < 0 or c < 0 or m > 3 or c > 3:
return False
if m > 0 and m < c:
return False
if (3 - m) > 0 and (3 - m) < (3 - c):
return False
return True

def solve_missionaries_cannibals():
start = (3, 3, 1)
goal = (0, 0, 0)
queue = deque([(start, [])])
visited = set()
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
while queue:
    (m, c, boat), path = queue.popleft()

    if (m, c, boat) == goal:
        return path + [(m, c, boat)]

    if (m, c, boat) in visited:
        continue
    visited.add((m, c, boat))
    current_path = path + [(m, c, boat)]
    for dm, dc in moves:
        if boat == 1:
            next_m, next_c, next_boat = m - dm, c - dc, 0
        else:
            next_m, next_c, next_boat = m + dm, c + dc, 1
        if is_safe(next_m, next_c):
            queue.append(((next_m, next_c, next_boat), current_path))
return None
if name == "main":
print("Solving Missionaries and Cannibals Problem...\n")
solution = solve_missionaries_cannibals()
if solution:
    print("Steps to transport everyone safely:")
    for step, (m, c, boat) in enumerate(solution):
        b_pos = "Left Bank" if boat == 1 else "Right Bank"
        print(f"Step {step}: Left Bank -> Missionaries: {m}, Cannibals: {c} | Boat: {b_pos}")
else:
    print("No solution exists.")
