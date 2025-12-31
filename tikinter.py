import tkinter as tk
root = tk.Tk()
root.title("SimpleCalculator")
root.configure(bg="black")
root.resizable(False,False)
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", padx=10, pady=10)

def button_click(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 0
col = 0

for btn in buttons:
    if btn == "=":
        tk.Button(button_frame, text=btn, width=5, height=2,
                  font=("Arial", 14), command=calculate)\
            .grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(button_frame, text=btn, width=5, height=2,
                  font=("Arial", 14),
                  command=lambda b=btn: button_click(b))\
            .grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root,
          text="C",
          width=20,
          height=2,
          bg="Red",
          font=("Arial", 14),
          command=clear_entry)\
    .pack(pady=10)

root.mainloop()
