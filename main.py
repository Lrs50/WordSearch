from tkinter import *
import pyglet
from ws_engine import * 
from tkinter import messagebox


def help1():
    txt="""
        Dimensão x refere-se ao número de colunas;
        
        Presione enter após modificar o valor das
        dimensões nas caixas de texto. 
    """
    messagebox.showinfo(title="Ajuda",message=txt)
def help2():
    txt="""
        Dimensão y refere-se ao número de linhas;
        
        Presione enter após modificar o valor das
        dimensões nas caixas de texto. 
    """
    messagebox.showinfo(title="Ajuda",message=txt)
def help3():
    txt="""
        Digite as palavras que serão adicionadas ao
        caça palavras, elas devem ser separadas por 
        uma vígula e não podem conter espaços vazios.
    """
    messagebox.showinfo(title="Ajuda",message=txt)
def help4():
    txt="""
        Cada caixa marcada refere-se a uma configuração
        do caça palavras.

        OBS: Mudar as configurações de formas inadequadas
        podem gerar erros durante a execução do programa.
    """
    messagebox.showinfo(title="Ajuda",message=txt)


def answer(ws_text,table):
    ws_text.delete("1.0",END)
    ws_text.insert(INSERT,table[1])
    ws_text.grid(row=0,column=0)
def view(ws_text,table):
    ws_text.delete("1.0",END)
    ws_text.insert(INSERT,table[0])
    ws_text.grid(row=0,column=0)

def word_search():

    ws_window=Toplevel()
    ws_window.title("WordSearch")
    ws_window.iconbitmap("ico/icon.ico")
    ws_window.minsize(width=250,height=120)
    ws_window.maxsize(width=1200,height=740)
    ws_window.resizable(0,0)
    ws_frame=LabelFrame(ws_window)
    ws_buttons=LabelFrame(ws_window)

    table,error=ws_engine(x_slider.get(),y_slider.get(),words_entry.get(),config_flags)

    ws_x=x_slider.get()
    ws_y=y_slider.get()

    if error==-1:
        ws_x=3
        ws_y=1


    ws_text=Text(ws_frame,height=ws_y,width=ws_x*2,font=("Courier Prime",9,"bold"))
    ws_text.insert(INSERT,table[0])
    answer_button=Button(ws_buttons,text="Resposta",command=lambda: answer(ws_text,table))
    table_button=Button(ws_buttons,text="Ver caça palavras",command=lambda: view(ws_text,table))

    ws_frame.pack(padx=10,pady=10)
    ws_buttons.pack(padx=10,pady=10)

    ws_text.grid(row=0,column=0)
    answer_button.grid(row=0,column=0,padx=10,pady=10)
    table_button.grid(row=0,column=1,padx=10)
    


def show_x(var):
    x_entry.delete(0,END)
    x_entry.insert(0,str(var))
def show_y(var):
    y_entry.delete(0,END)
    y_entry.insert(0,str(var))

def is_int(var):
    try:
        temp=int(var)
        if temp>100:
            temp=100
        elif temp<0:
            temp=0
        return temp
    except ValueError:
        messagebox.showerror("ValueError",str(var)+" is not a number!")
        return -1

def set_x():

    x=is_int(x_entry.get())
    if x!=-1:
        if x>70:
            x=70
    else:
        x=0
    x_slider.set(x)
    x_entry.delete(0,END)
    x_entry.insert(0,str(x))

def set_y():
    
    y=is_int(y_entry.get())
    if y!=-1:
        if y>40:
            y=40
    else:
        y=0
    y_slider.set(y)
    y_entry.delete(0,END)
    y_entry.insert(0,str(y))

#main
root=Tk()
root.title("WordSearch Generator ver:alpha0.1")
root.iconbitmap("ico/icon.ico")
root.geometry("600x280")
root.resizable(0,0)

#fonts
pyglet.font.add_file("fonts/CourierPrime-Bold.ttf")
pyglet.font.add_file("fonts/omegaflight3d.ttf")

#creating the frames
title_frame=LabelFrame(root,padx=5,pady=5)
options_frame=LabelFrame(root)
config_frame=LabelFrame(options_frame)

#config flags

config_flags=[IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar()]
config_flags[0].set(1)
config_flags[1].set(1)
config_flags[2].set(1)
config_flags[3].set(1)
config_flags[5].set(1)
#creating the Widgets
title1=Label(title_frame,text="WordSearch Generator",font=("Omega Flight 3D",20))
title2=Label(title_frame, text="ver:alpha0.1",font=("Helvetica",7))
opt1_label=Label(options_frame,text="Dimensão X:")
opt2_label=Label(options_frame,text="Dimensão Y:")
opt3_label=Label(options_frame,text="Palavras:")
opt4_label=Label(options_frame,text="Configurações:")
x_slider=Scale(options_frame,from_=0,to=70,orient=HORIZONTAL,showvalue=0,length=250,command=show_x)
y_slider=Scale(options_frame,from_=0,to=40,orient=HORIZONTAL,showvalue=0,length=250,command=show_y)
x_entry=Entry(options_frame,width=3)
y_entry=Entry(options_frame,width=3)
x_button=Button(options_frame,text="Enter",command=set_x)
y_button=Button(options_frame,text="Enter",command=set_y)
help1_button=Button(options_frame,text="Ajuda",command=help1)
help2_button=Button(options_frame,text="Ajuda",command=help2)
help3_button=Button(options_frame,text="Ajuda",command=help3)
help4_button=Button(options_frame,text="Ajuda",command=help4)
words_entry=Entry(options_frame)
check1_config=Checkbutton(config_frame,text="Horizontal",variable=config_flags[0])
check2_config=Checkbutton(config_frame,text="Vertical",variable=config_flags[1])
check3_config=Checkbutton(config_frame,text="Diagonal 1",variable=config_flags[2])
check4_config=Checkbutton(config_frame,text="Diagonal 2",variable=config_flags[3])
check5_config=Checkbutton(config_frame,text="Contrário",variable=config_flags[4])
check6_config=Checkbutton(config_frame,text="Maiúsculo",variable=config_flags[5])
check7_config=Checkbutton(config_frame,text="Minúsculo",variable=config_flags[6])
generate_button=Button(options_frame,text="Criar Caça-Palavras",command=word_search)



#config default
x_slider.set(10)
y_slider.set(10)

#rendering
title_frame.pack(pady=5)
title1.pack()
title2.pack()

options_frame.pack(pady=5)
opt1_label.grid(row=0,column=0,sticky=W)
opt2_label.grid(row=1,column=0,sticky=W)
opt3_label.grid(row=2,column=0,sticky=W)
opt4_label.grid(row=3,column=0,sticky=W)
x_slider.grid(row=0,column=1)
y_slider.grid(row=1,column=1)
x_entry.grid(row=0,column=3)
y_entry.grid(row=1,column=3)
x_button.grid(row=0,column=4,padx=5)
y_button.grid(row=1,column=4,padx=5)
help1_button.grid(row=0,column=5,padx=(0,5),pady=2)
help2_button.grid(row=1,column=5,padx=(0,5),pady=2)
help3_button.grid(row=2,column=5,padx=(0,5),pady=2)
help4_button.grid(row=3,column=5,padx=(0,5),pady=2)
words_entry.grid(row=2,column=1,columnspan=4,sticky=W+E,padx=(0,5))
config_frame.grid(row=3,column=1,columnspan=4,sticky=W+E,padx=(0,5))
check1_config.grid(row=0,column=0)
check2_config.grid(row=0,column=1)
check3_config.grid(row=0,column=2)
check4_config.grid(row=0,column=3)
check5_config.grid(row=1,column=0)
check6_config.grid(row=1,column=1)
check7_config.grid(row=1,column=2)
generate_button.grid(row=4,column=0,columnspan=6,pady=10)

root.mainloop()