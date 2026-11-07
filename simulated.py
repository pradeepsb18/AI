
import random
import math

# Calculate attacking queen pairs
def heuristic(board):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Display chessboard
def display(board):
    for row in range(8):
        for col in range(8):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Simulated Annealing
def simulated_annealing():

    board = [random.randint(0, 7) for _ in range(8)]

    temperature = 100
    cooling_rate = 0.95

    print("Initial Board:")
    display(board)

    step = 1

    while temperature > 0.1:

        current_h = heuristic(board)

        print("\nStep:", step)
        print("Heuristic:", current_h)
        print("Temperature:", round(temperature, 2))

        # Check goal state
        if current_h == 0:
            print("\nSolution Found!")
            display(board)
            return

        # Generate neighboring state
        new_board = board[:]

        col = random.randint(0, 7)
        row = random.randint(0, 7)

        new_board[col] = row

        new_h = heuristic(new_board)

        delta = new_h - current_h

        # Accept better state
        if delta < 0:
            board = new_board

        # Accept worse state with probability
        else:
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                board = new_board

        # Reduce temperature
        temperature = temperature * cooling_rate

        step += 1

    print("\nTemperature became low.")
    print("Final Heuristic:", heuristic(board))
    print("Final Board:")
    display(board)


# Main Program
simulated_annealing()
