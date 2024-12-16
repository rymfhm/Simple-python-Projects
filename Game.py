import tkinter as tk
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You Win!"
    else:
        return "Computer Wins!"

def play_game(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}")

def create_main_window():
    window = tk.Tk()
    window.title("Rock Paper Scissors")
    window.geometry("400x400")
    window.config(bg="lightgrey")

    title_label = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="lightgrey")
    title_label.pack(pady=20)

    button_frame = tk.Frame(window, bg="lightgrey")
    button_frame.pack(pady=20)

    rock_button = tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play_game("Rock"))
    rock_button.grid(row=0, column=0, padx=10)

    paper_button = tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play_game("Paper"))
    paper_button.grid(row=0, column=1, padx=10)

    scissors_button = tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play_game("Scissors"))
    scissors_button.grid(row=0, column=2, padx=10)

    global result_label
    result_label = tk.Label(window, text="", font=("Arial", 14), bg="lightgrey")
    result_label.pack(pady=20)

    window.mainloop()

def main():
    create_main_window()

if __name__ == "__main__":
    main()
