import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(expression)
            screen_var.set(result)
            expression = str(result)
        except:
            screen_var.set("Error")
            expression = ""
    
    elif text == "C":
        expression = ""
        screen_var.set("")
    
    else:
        expression += text
        screen_var.set(expression)

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("300x400")
root.configure(bg="#1e1e1e")

expression = ""
screen_var = tk.StringVar()

screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bg="#333", fg="white", justify="right")
screen.pack(fill="both", ipadx=8, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 14", width=5, height=2)
        b.pack(side="left", padx=5, pady=5)
        b.bind("<Button-1>", click)

root.mainloop()
