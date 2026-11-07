
import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Misplaced Tiles Heuristic
def misplaced(state):
    return sum(1 for i in range(9)
               if state[i] != 0 and state[i] != goal[i])


# Generate neighboring states
def neighbors(state):
    result = []
    zero = state.index(0)

    for move in [-3, 3, -1, 1]:
        new = zero + move

        if 0 <= new < 9:
            if move == -1 and zero % 3 == 0:
                continue
            if move == 1 and zero % 3 == 2:
                continue

            temp = list(state)
            temp[zero], temp[new] = temp[new], temp[zero]
            result.append(tuple(temp))

    return result


# A* Search
def astar(start):
    pq = [(misplaced(start), 0, start)]
    best_g = {start: 0}
    parent = {}

    while pq:
        f, g, current = heapq.heappop(pq)

        if g != best_g[current]:
            continue

        h = misplaced(current)

        print("\nCurrent State:")
        print(current[0:3])
        print(current[3:6])
        print(current[6:9])
        print("g(n) =", g)
        print("h(n) =", h)
        print("f(n) =", g + h)

        if current == goal:
            print("\nGoal State Reached!")
            path = []
            temp = current

            while temp in parent:
                path.append(temp)
                temp = parent[temp]

            path.append(start)

            print("\nSolution Path:")
            for state in reversed(path):
                print(state[0:3])
                print(state[3:6])
                print(state[6:9])
                print()
            return

        for nxt in neighbors(current):
            new_g = g + 1

            if new_g < best_g.get(nxt, float('inf')):
                best_g[nxt] = new_g
                parent[nxt] = current
                new_f = new_g + misplaced(nxt)
                heapq.heappush(pq, (new_f, new_g, nxt))


# Main Program
start = tuple(map(int, input(
    "Enter 9 numbers (0 for blank): "
).split()))

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input! Enter numbers 0 to 8 exactly once.")
else:
    astar(start)
