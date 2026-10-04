import heapq

GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

class PuzzleNode:
    def __init__(self, board, parent=None, move="", g=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.g = g  # Path cost
        self.h = self.get_manhattan_distance()
        self.f = self.g + self.h  # Total estimated cost

    def get_manhattan_distance(self):
        distance = 0
        
        targets = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 0: (2, 2)
        }
        for r in range(3):
            for c in range(3):
                val = self.board[r][c]
                if val != 0:  
                    tr, tc = targets[val]
                    distance += abs(r - tr) + abs(c - tc)
        return distance

    def __lt__(self, other):
        return self.f < other.f

    def find_blank(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    return r, c

    def get_neighbors(self):
        neighbors = []
        r, c = self.find_blank()
        
        moves = {
            "UP": (r - 1, c),
            "DOWN": (r + 1, c),
            "LEFT": (r, c - 1),
            "RIGHT": (r, c + 1)
        }

        for move_name, (nr, nc) in moves.items():
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_board = [list(row) for row in self.board]
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                board_tuple = tuple(tuple(row) for row in new_board)
                neighbors.append(PuzzleNode(board_tuple, self, move_name, self.g + 1))

        return neighbors


def solve(initial_board):
    start_node = PuzzleNode(initial_board)
    open_list = []
    heapq.heappush(open_list, start_node)
    closed_set = set()

    while open_list:
        current = heapq.heappop(open_list)

        if current.board == GOAL_STATE:
            path = []
            while current:
                path.append(current)
                current = current.parent
            return path[::-1]

        closed_set.add(current.board)

        for neighbor in current.get_neighbors():
            if neighbor.board in closed_set:
                continue
            heapq.heappush(open_list, neighbor)

    return None


def print_board(board):
    for row in board:
        print(" ".join(str(tile) if tile != 0 else "_" for tile in row))
    print()
if __name__ == "__main__":
    # 0 represents the blank space
    start_board = (
        (1, 2, 3),
        (0, 4, 6),
        (7, 5, 8)
    )
    print("Initial State:")
    print_board(start_board)

    solution = solve(start_board)
    if solution:
        print(f"Solved in {len(solution) - 1} moves!\n")
        for step, node in enumerate(solution):
            if step > 0:
                print(f"Step {step}: Move Blank {node.move}")
            print_board(node.board)
    else:
        print("No solution exists for this configuration.")

