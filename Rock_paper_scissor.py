import tkinter as tk
import random

moves = ["rock", "paper", "scissors"]

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("500x200")

root.config(bg="#ffffff")

user_move_label = tk.Label(root, text="Your move:", font=("Arial", 16), bg="#ffffff")
computer_move_label = tk.Label(root, text="Computer's move:", font=("Arial", 16), bg="#ffffff")
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#ffffff")

rock_button = tk.Button(root, text="Rock", command=lambda: play_move("rock"), font=("Arial", 16), bg="#8B7D6B")
paper_button = tk.Button(root, text="Paper", command=lambda: play_move("paper"), font=("Arial", 16), bg="#8cb3b8")
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_move("scissors"), font=("Arial", 16), bg="#0000FF")

user_move_label.grid(row=0, column=1, padx=10, pady=10)
computer_move_label.grid(row=2, column=1, padx=10, pady=10)
result_label.grid(row=3, column=0, padx=10, pady=10)
rock_button.grid(row=1, column=0, padx=10, pady=10)
paper_button.grid(row=1, column=1, padx=10, pady=10)
scissors_button.grid(row=1, column=2, padx=10, pady=10)


def play_move(move):

    computer_move = random.choice(moves)

    if move == computer_move:
        result = "It's a tie!"
    elif move == "rock" and computer_move == "scissors":
        result = "You win!"
    elif move == "paper" and computer_move == "rock":
        result = "You win!"
    elif move == "scissors" and computer_move == "paper":
        result = "You win!"
    else:
        result = "You lose!"

    computer_move_label.config(text="Computer's move: " + computer_move)
    result_label.config(text=result)

root.mainloop()
