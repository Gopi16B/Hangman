import tkinter as tk 
import random


window=tk.Tk()
window.title("Hangman Game")
window.minsize(width=200,height=300)
window.resizable(False,False)



words = ["PYTHON", "HANGMAN", "COMPUTER", "KEYBOARD", "PRINTER", "PROGRAM", "WINDOW", "MONITOR", "INTERNET", "NETWORK"]
word = random.choice(words).upper()
print(word)

underscores=" ".join(["_"]*len(word))


label=tk.Label(window,text=underscores,font=("Arial",27))
label.grid(row=0,column=2,padx=10,pady=10)



messagebox=tk.Entry(window,width=10,font=("Arial",24),justify="center",bg="lightgrey",fg="black")
messagebox.grid(row=1,column=2,padx=30,pady=30)

window.mainloop()