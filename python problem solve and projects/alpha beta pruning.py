import math
import random


def alpha_beta_pruning(node, level, alpha, beta, options, flag_max_min):
    if level == 3:
        return options[node]

    if flag_max_min:
        valid = -(math.inf)

        for i in range(2):
            value = alpha_beta_pruning(
                node * 2 + i, level + 1, alpha, beta, options, False
            )
            valid = max(valid, value)
            alpha = max(alpha, valid)

            if alpha >= beta:
                break
        return valid

    else:
        valid = math.inf
        for i in range(2):
            value = alpha_beta_pruning(
                node * 2 + i, level + 1, alpha, beta, options, True
            )
            valid = min(valid, value)
            beta = min(beta, valid)
            if alpha >= beta:
                break
        return valid


if __name__ == "__main__":
    points = []
    no_of_wins = 0
    id = input("Student ID: ")

    if len(id) != 8:
        raise ValueError("Invalid student id. Must be 8 digits.")

    if "0" in id:
        id = id.replace("0", "8")

    length = 8
    min_point = int(id[4])
    goal = int(id[-1] + id[-2])
    max_point = int(goal * 1.5)
    no_of_shuffles = int(id[3])

    for i in range(no_of_shuffles):
        options = random.sample(range(min_point, max_point), length)
        taken_value = alpha_beta_pruning(0, 0, -(math.inf), math.inf, options, True)
        points.append(taken_value)
        if taken_value >= goal:
            winner = "Optimus Prime"
            no_of_wins += 1
        else:
            winner = "Megatron"

        print("Generated 8 random points between minimum and maximum limits:")
        print(options)
        print(f"Total points to win: {goal}")
        print(f"Achieved point by applying Alpha-Beta pruning: {taken_value}")
        print(f"Winner is {winner}")
        print()

    print("List of all point values from each shuffles:")
    print(points)
    print(f"The maximum value of all shuffles: {max(points)}")
    print(f"Won {no_of_wins} times out of {no_of_shuffles} number of shuffles")
