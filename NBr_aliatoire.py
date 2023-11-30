import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de Devinette")
        self.master.geometry("300x150")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(self.master, text="Devinez le nombre:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(self.master, text="Devinez", command=self.check_guess)
        self.guess_button.pack(pady=10)

    def check_guess(self):
        user_guess = int(self.entry.get())
        self.attempts += 1

        if user_guess < self.number_to_guess:
            messagebox.showinfo("Résultat", "Le nombre à deviner est plus grand. Essayez à nouveau.")
        elif user_guess > self.number_to_guess:
            messagebox.showinfo("Résultat", "Le nombre à deviner est plus petit. Essayez à nouveau.")
        else:
            messagebox.showinfo("Félicitations", f"Vous avez deviné le nombre en {self.attempts} tentatives.")
            self.reset_game()

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
