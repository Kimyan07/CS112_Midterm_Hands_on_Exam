import random


def generate_question():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    operation = random.choice(['+', '-', '*', '/'])

    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    else:
        # For division, ensure the result is an integer and num2 is not zero
        num1, num2 = num1 * num2, num2  # Ensure num1 is divisible by num2
        answer = num1 // num2

    return f"What is {num1} {operation} {num2} ? ", answer


def main():
    num_questions = 5  # It's up to you if you want to change this to the desired number of questions

    for _ in range(num_questions):
        question, correct_answer = generate_question()
        user_answer = int(input(question))

        if user_answer == correct_answer:
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")


if __name__ == "__main__":
    main()
