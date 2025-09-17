import tkinter as tk 
import random


window=tk.Tk()
window.title("Hangman Game")
window.minsize(width=200,height=300)
window.resizable(False,False)



def reset_game():
    global word, underscores, tries
    word = random.choice(words).upper()
    underscores=" ".join(["_"]*len(word))
    label.config(text=underscores)







def ok():
    winning_popup.destroy()
    reset_game()





def Underscore():
    global underscores
    global underscores_list
    guess=messagebox.get().upper()
    for i in range(len(word)):
        if word[i]==guess:
            position=i*2
            underscores_list=list(underscores)
            underscores_list[position]=guess
            underscores="".join(underscores_list)
            label.config(text=underscores)
def exit1():
    winning_popup.destroy()
    window.destroy()


def SubAction():
    guess=messagebox.get().upper()
    print(guess)
    print(word)
    try1=len(word)
    position=word.find(guess)
    print(position)

    if guess == "":
        result_text.config(text="Please enter a letter")
    elif guess in word:
        result_text.config(text="Nice")
        Underscore()
        if "_" not in underscores:
            global winning_popup
            winning_popup=tk.Tk()
            winning_popup.title("You Win!")
            winning_popup.resizable(False,False)
            win_label=tk.Label(winning_popup,text="Congratulations! You guessed the word!",font=("Arial",14))
            win_label.pack(padx=20,pady=20)
            Again_button=tk.Button(winning_popup,text="OK",command=ok)
            Again_button.pack()
            # Exit_button=tk.Button(winning_popup,text="Exit",command=exit1)
            # Exit_button.pack()

            winning_popup.mainloop()
            
            

    else:
        result_text.config(text="Nope")




words = ["PYTHON", "HANGMAN", "COMPUTER", "KEYBOARD", "PRINTER", "PROGRAM", "WINDOW", "MONITOR", "INTERNET", "NETWORK"]
word = random.choice(words).upper()

underscores = " ".join(["_"]*len(word))


label=tk.Label(window,text=underscores,font=("Arial",27))
label.grid(row=0,column=2,padx=10,pady=10)



messagebox=tk.Entry(window,width=10,font=("Arial",24),justify="center",bg="lightgrey",fg="black")
messagebox.grid(row=1,column=2,padx=30,pady=30)

submit=tk.Button(window,text="Submit",font=("Arial",14), command=SubAction)
submit.grid(row=2,column=2) 

result_text=tk.Label(window,text="")
result_text.grid(row=3,column=2)


tries=len(word)-1

tries_text=tk.Label(window)
tries_text.grid(row=4,column=2)


window.mainloop()