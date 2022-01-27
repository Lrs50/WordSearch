from PIL import Image,ImageFont,ImageDraw
from tkinter import *
from tkinter.filedialog import asksaveasfile





def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files)


root = Tk() 
root.geometry('200x150') 





img=Image.new("RGBA",(900,900),"white")
str1="""hello
        There"""

font=ImageFont.truetype("arial.ttf",75)
w,h=font.getsize(str1)

draw=ImageDraw.Draw(img)
draw.text(((900-w)/2,(900-h)/2),str1,font=font,fill="black")

#img.show()

#img.save("S:/Images/test.png")


btn = ttk.Button(root, text = 'Save', command = lambda : save()) 
btn.pack(side = TOP, pady = 20) 

mainloop() 