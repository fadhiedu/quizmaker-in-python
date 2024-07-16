import tkinter as tk
from tkinter import messagebox
import json

class QuizMaker:
    def __init__(self, root, filename):
        self.root = root
        self.filename = filename
        self.questions = self.read_questions()
        self.current_question = 0
        self.score = 0

        self.root.configure(bg="#2f2f2f")  # Set background color to dark gray

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Helvetica", 18), fg="#ffffff", bg="#2f2f2f")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 18), fg="#ffffff", bg="#333333", highlightthickness=0, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 18), fg="#ffffff", bg="#2f2f2f")
        self.score_label.pack(pady=20)

        self.next_question()

    def read_questions(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def next_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.config(text=question["question"])
            for i, option in enumerate(question["options"]):
                self.option_buttons[i].config(text=option)
            self.current_question += 1
        else:
            self.question_label.config(text="Quiz complete!")
            for button in self.option_buttons:
                button.config(state="disabled")
            self.score_label.config(text=f"Score: {self.score}")

    def check_answer(self, option_index):
        question = self.questions[self.current_question-1]
        if question["options"][option_index] == question["answer"]:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is {question['answer']}.")
        self.next_question()

root = tk.Tk()
root.title("Quiz Maker")
root.geometry("500x400")  # Set window size
root.resizable(False, False)  # Disable window resizing

quiz_maker = QuizMaker(root, "Downloads\qiuz.json")
root.mainloop()