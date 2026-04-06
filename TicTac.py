import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for combo in winning_combinations:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            
            # Highlight winner
            for i in combo:
                buttons[i].config(bg="green")
            
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            winner = True
            return
    
    # ✅ Draw detection
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        winner = True


def button_click(index):
    global winner
    
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        
        if not winner:
            toggle_player()


def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")


# ✅ Restart function
def restart_game():
    global current_player, winner
    
    current_player = "X"
    winner = False
    
    for button in buttons:
        button.config(text="", bg="SystemButtonFace")
    
    label.config(text=f"Player {current_player}'s turn")


# GUI Setup
root = tk.Tk()
root.title("TicTacToe")

buttons = [
    tk.Button(root, text="", font=("normal",25), width=6, height=2,
              command=lambda i=i: button_click(i))
    for i in range(9)
]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"
winner = False

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

# ✅ Restart Button
restart_btn = tk.Button(root, text="Restart Game", font=("normal", 14), command=restart_game)
restart_btn.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()