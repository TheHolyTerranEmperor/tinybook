import os
import tkinter as tk

base_directory = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()#we need to remove 
main.title("Main Window thing")
main.config(bg="#E4E2E2")
main.geometry("250x122")

menu = tk.Menu(main)
main.config(menu=menu)

frame = tk.Frame()
frame.Place(x=0, y=0, width=250, height=122)

main.mainloop()