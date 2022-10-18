import tkinter as tk
import tkinter.messagebox as tkm
from tokenize import maybe
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def count_up():
    global tmr
    tmr+=1
    label["text"] = tmr
    root.after(1000,count_up)

def main_proc():
    global mx,my
    global cx,cy

    if key=="Up" and maze_lst[my-1][mx]!=1:
        my-=1
    elif key=="Down" and maze_lst[my+1][mx]!=1:
        my+=1
    elif key=="Left" and maze_lst[my][mx-1]!=1:
        mx-=1
    elif key=="Right" and maze_lst[my][mx+1]!=1:
        mx+=1

    if maze_lst[my][mx] != 1:
        cx,cy=mx*100+50,my*100+50
    
    canv.coords("gomi",cx,cy)
    root.after(100, main_proc)
    
if __name__ == "__main__":
    root=tk.Tk()
    root.title("ごみを捨てよう")
    label = tk.Label(root,font=("",80))
    label.pack()

    canv = tk.Canvas(
        root,
        width=1500,
        height=900,
        bg='black'
    )
    canv.pack()
    
    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canv,maze_lst)

    gomi = tk.PhotoImage(file="fig/gomibukuro_yellow.png")
    gomi = gomi.subsample(7)
    mx,my=1,1
    cx,cy=300,400
    canv.create_image(cx,cy,image=gomi,tag="gomi")

    key=""
    tmr = 0

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    
    count_up()
    
    main_proc() 

    
    root.mainloop()