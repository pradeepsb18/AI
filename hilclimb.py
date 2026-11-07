
import random

def heuristic(board):
    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def print_board(board):
    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def hill_climbing(n):
    step = 1

    while True:
        board = [random.randint(0, n - 1) for _ in range(n)]

        print("\nInitial State:")
        print_board(board)

        while True:
            current_h = heuristic(board)

            print("\nStep", step)
            print("Current Heuristic:", current_h)

            if current_h == 0:
                print("\nSolution Found!")
                return board

            best_board = board[:]
            best_h = current_h

            for col in range(n):
                for row in range(n):
                    new_board = board[:]
                    new_board[col] = row

                    h = heuristic(new_board)

                    if h < best_h:
                        best_h = h
                        best_board = new_board

            if best_h == current_h:
                print("Local optimum reached. Restarting...")
                break

            board = best_board

            print("Best Neighbor:")
            print_board(board)
            print("New Heuristic:", best_h)

            step += 1


# Main Program
n = int(input("Enter number of queens: "))

if n < 1:
    print("Enter a positive number")
else:
    solution = hill_climbing(n)

    print("\nFinal Solution:")
    print_board(solution)

    print("Final Heuristic:", heuristic(solution))
