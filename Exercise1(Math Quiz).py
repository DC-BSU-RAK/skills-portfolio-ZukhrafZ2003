import tkinter as tk
from tkinter import messagebox
import random

# ===== FUNCTIONS =====

def displayMenu():
    """Display difficulty level menu using Labels and Buttons"""
    clear_window()

    title_label = tk.Label(root, text=" ARITHMETIC QUIZ ", 
                           font=("Arial", 22, "bold"), bg="#a2d2ff")
    title_label.pack(pady=20)

    instruction_label = tk.Label(root, text="Select Difficulty Level", 
                                 font=("Arial", 16), bg="#a2d2ff")
    instruction_label.pack(pady=10)

    # Buttons to choose difficulty
    tk.Button(root, text="Easy (1-digit)", font=("Arial", 14), bg="#bde0fe",
              command=lambda: start_quiz("easy")).pack(pady=5)
    tk.Button(root, text="Moderate (2-digit)", font=("Arial", 14), bg="#bde0fe",
              command=lambda: start_quiz("moderate")).pack(pady=5)
    tk.Button(root, text="Advanced (4-digit)", font=("Arial", 14), bg="#bde0fe",
              command=lambda: start_quiz("advanced")).pack(pady=5)


def randomInt(level):
    """Return random integers based on difficulty level"""
    if level == "easy":
        return random.randint(1, 9)
    elif level == "moderate":
        return random.randint(10, 99)
    elif level == "advanced":
        return random.randint(1000, 9999)


def decideOperation():
    """Randomly choose addition or subtraction"""
    return random.choice(["+", "-"])


def displayProblem():
    """Display one arithmetic question"""
    global num1, num2, operation, attempts

    attempts = 0
    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operation = decideOperation()

    clear_window()

    # Label for question number
    question_label = tk.Label(root, text=f"Question {current_question + 1} of 10",
                              font=("Arial", 16, "italic"), bg="#a2d2ff")
    question_label.pack(pady=10)

    # Label for math problem
    problem_label = tk.Label(root, text=f"{num1} {operation} {num2} = ?", 
                             font=("Arial", 20, "bold"), bg="#a2d2ff")
    problem_label.pack(pady=20)

    # Entry for user's answer
    global answer_entry
    answer_entry = tk.Entry(root, font=("Arial", 16))
    answer_entry.pack(pady=10)
    answer_entry.focus()

    # Button for submitting answer
    submit_button = tk.Button(root, text="Submit", font=("Arial", 14, "bold"), 
                              bg="#bde0fe", command=checkAnswer)
    submit_button.pack(pady=10)


def isCorrect(user_answer):
    """Check if user's answer is correct"""
    correct_answer = num1 + num2 if operation == "+" else num1 - num2
    return user_answer == correct_answer


def checkAnswer():
    """Handle answer checking, scoring, and next question logic"""
    global score, current_question, attempts

    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showwarning("Invalid", "Please enter a valid number.")
        return

    if isCorrect(user_answer):
        # Award points based on attempt number
        if attempts == 0:
            score += 10
            messagebox.showinfo("Correct!", " Correct! (+10 points)")
        else:
            score += 5
            messagebox.showinfo("Correct!", " Correct on 2nd try! (+5 points)")

        current_question += 1
        if current_question < 10:
            displayProblem()
        else:
            displayResults()
    else:
        # If wrong, allow one retry
        if attempts == 0:
            attempts += 1
            messagebox.showwarning("Try Again", " Incorrect! Try once more.")
        else:
            messagebox.showinfo("Incorrect", " Wrong again! Moving to next question.")
            current_question += 1
            if current_question < 10:
                displayProblem()
            else:
                displayResults()


def displayResults():
    """Display final score and rank"""
    clear_window()

    # Rank calculation
    if score >= 90:
        rank = "A+"
    elif score >= 80:
        rank = "A"
    elif score >= 70:
        rank = "B"
    elif score >= 60:
        rank = "C"
    else:
        rank = "D"

    # Labels for results
    result_label = tk.Label(root, text=" QUIZ COMPLETE! ", 
                            font=("Arial", 20, "bold"), bg="#a2d2ff")
    result_label.pack(pady=20)

    score_label = tk.Label(root, text=f"Your Final Score: {score} / 100", 
                           font=("Arial", 16), bg="#a2d2ff")
    score_label.pack(pady=10)

    rank_label = tk.Label(root, text=f"Your Rank: {rank}", 
                          font=("Arial", 16, "bold"), bg="#a2d2ff")
    rank_label.pack(pady=10)

    # Buttons to replay or exit
    tk.Button(root, text="Play Again", font=("Arial", 14), bg="#bde0fe", 
              command=displayMenu).pack(pady=10)
    tk.Button(root, text="Exit", font=("Arial", 14), bg="#bde0fe", 
              command=root.destroy).pack(pady=10)


def start_quiz(level):
    """Initialize quiz variables and start"""
    global difficulty, score, current_question
    difficulty = level
    score = 0
    current_question = 0
    displayProblem()


def clear_window():
    """Clear all widgets from window"""
    for widget in root.winfo_children():
        widget.destroy()


# ===== MAIN WINDOW =====
root = tk.Tk()
root.title("Arithmetic Quiz")
root.geometry("500x400")
root.configure(bg="#a2d2ff")

displayMenu()

root.mainloop()

