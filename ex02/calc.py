import numbers
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}",f"{num}ボタンが押されました")
    entry.insert(tk.END,num)

root = tk.Tk()
root.title("練習問題1")
root.geometry("300x500")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=3)

r,c = 1,0
numbers = list(range(9,-1,-1))
operators = ["+"]
for i,num in enumerate(numbers+operators,1):
    button = tk.Button(root, text=f"{num}",font=("",30),width="4",height="2")
    button.bind("<1>",button_click)
    button.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0


root.mainloop()