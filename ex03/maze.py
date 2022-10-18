import tkinter as tk
import tkinter.messagebox as tkm
from tokenize import maybe
import maze_maker as mm


global key

def key_down(event):
    global key
    key = event.keysym
    #tkm.showinfo("キー押下",f"{key}キーが押されました")

def key_up(event):
    global key
    key = ""
    #tkm.showinfo("キー押下",f"{key}キーが押されました")

def main_proc():
    global mx,my
    global cx,cy

    if key=="Up" and maze_lst[my-1][mx]==0:
        my-=1
    elif key=="Down" and maze_lst[my+1][mx]==0:
        my+=1
    elif key=="Left" and maze_lst[my][mx-1]==0:
        mx-=1
    elif key=="Right" and maze_lst[my][mx+1]==0:
        mx+=1

    if maze_lst[my][mx] == 0:
        cx,cy=mx*100+50,my*100+50
    
    canv.coords("tori",cx,cy)
    root.after(100, main_proc)

def key_down(event):
    global jid
    if jid != None:
        root.after_cancel(jid)
        jid = None
        return
    key = event.keysym
    jid = root.after(1000,count_up)

def count_up():
    global tmr,jid
    tmr+=1
    label["text"] = tmr
    jid = root.after(1000,count_up)

    
if __name__ == "__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん")
    label = tk.Label(root,font=("",80))
    label.pack()

    tmr = 0
    jid = None
    root.bind("<KeyPress>",key_down)

    canv = tk.Canvas(
        root,
        width=1500,
        height=900,
        bg='black'
    )
    canv.pack()
    
    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canv,maze_lst)

    tori = tk.PhotoImage(file="fig/gomibukuro_yellow.png")
    tori = tori.subsample(8)
    mx,my=1,1
    cx,cy=300,400
    canv.create_image(cx,cy,image=tori,tag="tori")

    key=""

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    
    main_proc() 

    
    root.mainloop()