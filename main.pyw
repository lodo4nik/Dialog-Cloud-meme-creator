from cgitb import text
from tkinter.ttk import Combobox
from PIL import Image
import requests
from tkinter import Checkbutton, IntVar, Tk, Label, Entry, Button
import os

def putCloud():
    try:
        url = txt.get()
        type = combo.get()
        reversed = i.get()
        response = requests.get(url, stream = True).raw
        inimage = Image.open(response)
        filename = txt_filename.get()


        if type == "Round":
            cloud = Image.open("cloud.png")
        elif type == "Box":
            cloud = Image.open("cloud2.png").convert("RGBA")
        elif type == "Center":
            cloud = Image.open("cloud3.png")


        cloud = cloud.resize((inimage.width, round(inimage.height/2.5)), Image.BILINEAR)
        if reversed == 1:
            cloud = cloud.transpose(Image.TRANSPOSE.FLIP_LEFT_RIGHT)
        else:
            pass
        inimage.paste(cloud, (0, 0), cloud)
        inimage.save(filename + ".gif")
        res = "Saved as " + os.path.abspath(filename + ".gif")
        lbl_saved.configure(text=res, font=("Lucida Console", 12), fg="green", textvariable=text, wraplength=350)

    except:
        res = "Error!"
        lbl_saved.configure(text=res, font=("Lucida Console", 12), fg="red", textvariable=text, wraplength=350)




window = Tk()
window.iconbitmap("icon.ico")
window.resizable(False, False)
window.title("Dialog cloud meme creator")
window.geometry("400x280")

i = IntVar()

lbl = Label(window, 
            text="Paste image link here: ", 
            padx="90",
            pady="8",
            font=("Arial Bold", 16))
txt = Entry(window,width=40)  
txt.grid(row=3)
lbl.grid(column=0, row=0)


c = Checkbutton(window, text = "Reverse", variable=i)
c.grid(column=0, row=4)

combo = Combobox(window)  
combo['values'] = ("Cloud type", "Round", "Box", "Center")  
combo.current(0)
combo.grid(column=0, row=5)  


but = Button(window, 
            text ="Put cloud!", 
            command = putCloud,
            padx="16",
            pady="10",
            )
but.place(x=150, y=220)
lbl_saved = Label(window, text="<==Status==>", font=("Lucida Console", 12), textvariable=text, wraplength=350)
lbl_saved.grid(column=0, row=6)

lbl_filename = Label(window, text="Filename: ")
lbl_filename.place(x=110, y=200)

txt_filename = Entry(window, width=18)
txt_filename.place(x=180, y=200)

window.mainloop()


#128 - 81