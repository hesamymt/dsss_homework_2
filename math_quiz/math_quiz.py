import random


def randomNumberLimit(min, max):
    # """
    # generate a random integer between 'min' and 'max' (inclusive).
    # """
    return random.randint(min, max)


def randomOperator():
    # """
    # Select a random arithmetic operator from the set {+, -, *}.
    # """

    return random.choice(['+', '-', '*'])


def calculateFunc(n1, n2, operator):
    # """
    # Calculate the result of a mathematical operation.
    # """
    problem = f"{n1} {operator} {n2}"
    if operator == '+': answer = n1 + n2
    elif operator == '-': answer = n1 - n2
    else: answer = n1 * n2
    return problem, answer

def math_quiz():
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = randomNumberLimit(1, 10); n2 = randomNumberLimit(1, 5); operator = randomOperator()

        PROBLEM, ANSWER = calculateFunc(n1, n2, operator)
        print(f"\nQuestion: {PROBLEM}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0  # default value for user_answer to prevent crashing.

        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
