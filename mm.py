import tkinter as tk
import TTT
import MOVIE
import JUMBLE
import BATTLESHIP
import DOBBLE
            
root= tk.Tk()                               
root.title("GAME WORLD")                                #To give title to the root window
root.geometry('1800x1600')

l1 = tk.Label(root, text="Game World",bg="blue",width=30,height=2)
l1.pack()

def game_1():
    TTT.ttt.playplay()
    return
def game_2():
    MOVIE.Movie.palyplay()
    return
def game_3():
    JUMBLE.Jumble.playplay()
    return
def game_4():
    BATTLESHIP.Battleship.playplay()
    return
def game_5():
    DOBBLE.Dobble.playplay()
    return
def close_window(root): 
    root.destroy()


b1=tk.Button(root, text= "TIC TAC TOE", fg= "blue", command=game_1,width=30,height=2)
b1.pack()
b2=tk.Button(root,text="MOVIE GUESS", fg="blue", command=game_2,width=30,height=2)
b2.pack()

b3=tk.Button(root, text= "JUMBLED WORDS", fg= "blue", command=game_3,width=30,height=2)
b3.pack()
b4=tk.Button(root,text="BATTLESHIP", fg="blue", command=game_4,width=30,height=2)
b4.pack()

b5=tk.Button(root, text= "DOBBLE GAME", fg= "blue", command=game_5,width=30,height=2)
b5.pack()
b6=tk.Button(root,text="EXIT", fg="blue", command=close_window , width=30,height=2)
b6.pack()


l1.place(x=650,y=260)
b1.place(x=500, y=360)
b2.place(x=790, y=360)
b3.place(x=500,y=420)
b4.place(x=790, y=420)
b5.place(x=500, y=490)
b6.place(x=790, y=490)

root.mainloop()
