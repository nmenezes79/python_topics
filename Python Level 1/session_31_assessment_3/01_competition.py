import random
import time

def math_quiz():
    score = 0
    total_time = 0

    print("Welcome to the Math Quiz Competition!")
    print("You will get 10 questions. Try to answer as quickly and correctly as possible.\n")

    for i in range(1, 11):
        # Generate random numbers and operation
        num1 = random.randint(10, 999)
        num2 = random.randint(10, 999)
        operation = random.choice(["+", "-"])

        # Create question and calculate correct answer
        if operation == "+":
            correct_answer = num1 + num2
        else:
            correct_answer = num1 - num2

        print(f"Q{i}: {num1} {operation} {num2} = ?")

        # Start time
        start_time = time.time()

        # Take user answer (handle invalid input safely)
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Counting as wrong.")
            user_answer = None

        # End time
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        total_time += time_taken

        # Check correctness
        if user_answer == correct_answer:
            print(f"✅ Correct! Time taken: {time_taken} seconds\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was {correct_answer}. Time taken: {time_taken} seconds\n")

    # Final result
    print("----- Quiz Completed -----")
    print(f"Your Score: {score}/10")
    print(f"Total Time Taken: {round(total_time, 2)} seconds")

# Run the quiz
math_quiz()
