# 13_inclass_challenge_quiz_game.py

import tkinter as tk
from tkinter import ttk

class QuizGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("400x350")

        self.questions = [
            {
                "question": "How many Colors are there in a Rainbow?",
                "options": ["6", "7", "8", "5"],
                "correct_answer": "7"
            },

            {
                "question": "What is the Largest Mammal in the World?",
                "options": ["Elephant", "Giraffe", "Lion", "Blue Whale"],
                "correct_answer": "Blue Whale"
            },

            {
                "question": "Which one is a Programming Language?",
                "options": ["HTML", "CSS", "Python", "JavaScript"],
                "correct_answer": "Python"
            }
        ]

        self.current_question_index = 0
        self.score = 0

        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.label_question = ttk.Label(self.master, text="", font=("Arial", 12), wraplength=380)
        self.label_question.pack(pady=10)

        self.radio_var = tk.IntVar(value=-1)
        self.radio_buttons = []
        for i in range(4):
            radio_button = ttk.Radiobutton(self.master, text="", variable=self.radio_var, value=i)
            radio_button.pack(anchor="w")
            self.radio_buttons.append(radio_button)

        self.next_button = ttk.Button(self.master, text="Next", command=self.check_answer)
        self.next_button.pack(pady=5)

        self.reset_button = ttk.Button(self.master, text="Reset", command=self.reset_quiz)
        self.reset_button.pack(pady=5)

        self.result_label = ttk.Label(self.master, text="")
        self.result_label.pack()

    def display_question(self):
        question = self.questions[self.current_question_index]
        self.label_question.config(text=question["question"])  # fixed spelling

        options = question["options"]
        for i, option in enumerate(options):
            self.radio_buttons[i].config(text=option)

    def check_answer(self):
        selected_index = self.radio_var.get()
        if selected_index != -1:
            selected_option = self.questions[self.current_question_index]["options"][selected_index]  # fixed
            correct_answer = self.questions[self.current_question_index]["correct_answer"]
            if selected_option == correct_answer:
                self.score += 1

            self.current_question_index += 1
            if self.current_question_index < len(self.questions):
                self.display_question()
                self.radio_var.set(-1)
            else:
                self.show_result()
                self.next_button.config(state="disabled")
        else:
            self.result_label.config(text="Please Select an Answer.")  # fixed typo

    def show_result(self):
        total_question = len(self.questions)
        result_message = f"You answered {self.score} out of {total_question} questions correctly."
        self.result_label.config(text=result_message)

    def reset_quiz(self):
        self.current_question_index = 0
        self.score = 0
        self.display_question()
        self.result_label.config(text="")
        self.next_button.config(state="normal")  # fixed state
        self.radio_var.set(-1)

def main():
    root = tk.Tk()
    app = QuizGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
