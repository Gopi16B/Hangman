import tkinter as tk

button_values = [
    ["%", "+/-","AC", "÷"],     
        ["7", "8", "9", "x"], 
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "√", "="]
    ]

right_symbols = ["÷", "x", "-", "+", "=","√"]
top_symbols = ["AC", "+/-", "%"]


row_count = len(button_values)
column_count = len(button_values[0])


color_light_grey = "#D4D4D2"
color_black = "#1C1C1C"
color_light_grey="#8F8E8E"
color_dark_grey="#292929"
color_white="white"
color_orange = "#FF9F22"

window = tk.Tk()
window.title("Calculator")
window.resizable(False,False)



frame= tk.Frame(window)
frame.pack()
label = tk.Label(frame, text="0",font=("Arial", 45),background=color_black,foreground=color_white, anchor="e",width=column_count)
label.pack()
label.grid(row=0,column=0,columnspan=column_count,sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tk.Button(frame, text=value,font=("Arial",24),bd=1,highlightthickness=0, width=column_count-1,height=2,command=lambda value=value: button_clicked(value))
        
        if value in top_symbols:
            button.config(background=color_light_grey,foreground=color_black)
            
        elif value in right_symbols:
            if value in "√":
                button.config(background=color_dark_grey,foreground=color_white)
            else:
                button.config(background=color_orange,foreground=color_white)
        
        else:
            button.config(background=color_dark_grey,foreground=color_white)
        
        
        
        button.grid(row=row+1, column=column)
        
        
a="0" 
b=None
operators=None

def clear_all():
    global a, b , operators
    a="0" 
    b=None
    operators=None
    
def remove_decimal(num):
    if num % 1==0:
        num=int(num)
    return str(num)
        
def button_clicked(value):
    global right_symbols,top_symbols,operators,a,b,label
    
    if value in top_symbols:
            if value=="AC":
                clear_all()
                label["text"]="0"
            
            elif value=="+/-":
                result = float(label["text"])*-1
                label["text"]=remove_decimal(result)
        
                    
            else:
                perc=float(label["text"])/100
                label["text"]=remove_decimal(perc)
        
    elif value in right_symbols:
            if value =="=":
                if a is not None and operators is not None:
                    b=label["text"]
                    num1=float(a)
                    num2=float(b)
                    
                    if operators=="+":
                        result=num1+num2
                    elif operators=="x":
                        result=num1*num2
                        
                    elif num2!=0 and operators=="÷":
                        result=num1/num2

                    elif operators=="-":
                        result=num1-num2
                    
                    elif value =="√":
                        result = float(label["text"])**0.5
                        label["text"]=remove_decimal(result)
                    

                    else:
                        label["text"]="error"
                        
                    label["text"]=remove_decimal(result)
                    clear_all()
                    
            elif value =="√":
                result = float(label["text"])**0.5
                label["text"]=remove_decimal(result)
                clear_all()
                        
                    
            elif value in "+-x÷":
                if operators is None:
                    a=label["text"]
                    label["text"]="0"
                    b="0"
                    
            operators=value
                
    
    else:
        if value == ".":
            if value not in label["text"]:
                label["text"]+=value
        
        elif value in "0123456789":
            if label["text"]=="0":
                label["text"]=value
            else:
                label["text"]+=value
    
    
    
    
    
    
window.resizable(False,False)
window.mainloop()


