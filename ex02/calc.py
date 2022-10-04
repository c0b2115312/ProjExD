from cgitb import reset
import numbers
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(f"{num}",f"{num}ボタンが押されました")
    entry.insert(tk.END,num)

def equal_click(event):
    eqn = entry.get()
    eqn = eqn.replace("÷", "/")#掛け算、割り算の文字の置き換え
    eqn = eqn.replace("×", "*")
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)

#マウスオーバー色
def enter_bg(event):
    event.widget['bg'] = '#FDF5E6'

def leave_bg(event):
    event.widget['bg'] = '#FFFFFF'

#式をリセット
def reset(event):
    entry.delete(0, tk.END)





root = tk.Tk()
root.title("電卓")
root.geometry("400x600")

entry = tk.Entry(root, width=10, font=(", 40"), justify="right") # 練習4
entry.grid(row=0, column=0, columnspan=3)

r,c = 1,0
numbers = [
        7,8,9,"+",
        4,5,6,"-",
        1,2,3,"×",
        "C",0,"=","÷"
]

for i,num in enumerate(numbers,1):
    button = tk.Button(root,bg="#FFFFFF" ,text=f"{num}",font=("",30),width="4",height="1")
    button.bind("<1>",button_click)

    if num=="=":
        button = tk.Button(root, text=f"=",bg="#FFFFFF",font=("",30),width="4",height="1")
        button.bind("<1>",equal_click)

    if num=="C":
        button = tk.Button(root, text=f"AC",bg="#FFFFFF",font=("",30),width="4",height="1")
        button.bind("<1>",reset)

    #掛け算、割り算の置き換え
    if num=="×":
        button = tk.Button(root, text=f"×",bg="#FFFFFF",font=("",30),width="4",height="1")
        button.bind("<1>",equal_click)

    if num=="÷":
        button = tk.Button(root, text=f"÷",bg="#FFFFFF",font=("",30),width="4",height="1")
        button.bind("<1>",equal_click)
    



    #ボタンの色変える
    button.bind("<Enter>", enter_bg)
    button.bind("<Leave>", leave_bg)

    
    
    button.grid(row=r, column=c)
    c += 1
    if i%4 == 0:
        r += 1
        c = 0

root.mainloop()