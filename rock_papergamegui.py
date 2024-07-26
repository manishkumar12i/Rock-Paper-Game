import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissor:
    def __init__(self, window):
        self.window = window
        self.window.title("Rock Paper Scissors Game")
        self.window.geometry('400x400')
        self.window.resizable(False, False)
        self.window.config(background='purple')
        
        self.user_score = 0
        self.computer_score = 0
        
        self.title_label = tk.Label(self.window, text="Rock Scissor Game", font=("Helvetica", 22), fg="white", bg='purple')
        self.title_label.pack(pady=10)
        
        self.user_score_label = tk.Label(self.window, text=f"Your Score: {self.user_score}", font=("Helvetica", 12), fg="white", bg='purple')
        self.user_score_label.pack()
        
        self.computer_score_label = tk.Label(self.window, text=f"Opponent Score: {self.computer_score}", font=("Helvetica", 12), fg="white", bg='purple')
        self.computer_score_label.pack()
        
        self.rock_button = tk.Button(self.window, text="Rock", width=20, bd=5, font=('times new roman', 12, 'bold'), bg='black', fg='gold', command=lambda: self.handle_click("Rock"), cursor='hand2')
        self.rock_button.pack(pady=10)
        
        self.paper_button = tk.Button(self.window, text="Paper", width=20, bd=5, font=('times new roman', 12, 'bold'), bg='black', fg='gold', command=lambda: self.handle_click("Paper"), cursor='hand2')
        self.paper_button.pack(pady=10)
        
        self.scissors_button = tk.Button(self.window, text="Scissors", width=20, bd=5, font=('times new roman', 12, 'bold'), bg='black', fg='gold', command=lambda: self.handle_click("Scissors"), cursor='hand2')
        self.scissors_button.pack(pady=10)


    def get_computer_choice(self):
        choices = ['Rock', 'Paper', 'Scissors']
        return random.choice(choices)

    def determine_winner(self,user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
         self.user_score += 1
         return "You win!"
        else:
            self.computer_score +=1
            return "You lose!"

    def update_score_board(self):
        self.user_score_label.config(text=f'Your Score 🎯 {self.user_score}')
        self.computer_score_label.config(text=f'Opponent Score 🎯  {self.computer_score}')
    def play_game(self,user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        messagebox.showinfo("Result", f"Your choice: {user_choice}\nOpponent's choice: {computer_choice}\n\n{result}")
        self.update_score_board()

    def handle_click(self,choice):
        self.play_game(choice)

window = tk.Tk()
game = RockPaperScissor(window)
window.mainloop()