
import pygame

from tkinter import*
from tkinter import filedialog

import os
from PIL import Image,ImageTk

pygame.mixer.init()


songs=[]
i=0
count=0
def play_fnc():
    global i
    song=Songs_list.get(ACTIVE)
    i=Songs_list.get(0,END).index(song)
    pygame.mixer.music.load(str(songs[i]))
    pygame.mixer.music.play(0)
   
    
    

def forward_fnc():
    global i
    i=(i+1)%(len(songs))
    pygame.mixer.music.load(str(songs[i]))
    pygame.mixer.music.play(0)

def back_fnc():
    global i
    i=i-1
    if(i<0):
        i=len(songs)-1
    else:
        i=i%(len(songs))
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play(0)

def pause_fnc():
    global i
    global count
    count=count+1
    if count%2!=0:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
       
def add_fnc():
    song=filedialog.askopenfilename(filetypes=(("mp3 Files","*.mp3"),))
    songs.insert(len(songs),song)
    song_to_listbox=os.path.basename(song)
    song_to_listbox=song_to_listbox.replace(".mp3"," ")
    Songs_list.insert(END,song_to_listbox)

def rem_fnc():
    song=Songs_list.get(ACTIVE)
    pos=Songs_list.get(0,END).index(song)
    Songs_list.delete(pos)
    songs.pop(pos)

  






root=Tk()
root.geometry("600x600+500+100")
image1 = Image.open("bg.webp").resize((600,600),Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = Label(image=test)
label1.image = test
label1.place(x=0, y=0)

Songs_list=Listbox(root) 
Songs_list.pack()


Back_image=Image.open("1.PNG").resize((50,50),Image.ANTIALIAS)
Forward_image=Image.open("4.PNG").resize((50,50),Image.ANTIALIAS)
Pause_unpause_image=Image.open("2.PNG").resize((50,50),Image.ANTIALIAS)
Play_image=Image.open("3.PNG").resize((50,50),Image.ANTIALIAS)

Back_image=ImageTk.PhotoImage(Back_image)
Forward_image=ImageTk.PhotoImage(Forward_image)
Pause_unpause_image=ImageTk.PhotoImage(Pause_unpause_image)
Play_image=ImageTk.PhotoImage(Play_image)


button_frame= Frame(root)
button_frame.pack(pady=30)


back_btn=Button(button_frame,image=Back_image,borderwidth=0,command=back_fnc)
forward_btn=Button(button_frame,image=Forward_image,borderwidth=0,command=forward_fnc)
play_btn=Button(button_frame,image=Play_image,borderwidth=0,command=play_fnc)
pause_btn=Button(button_frame,image=Pause_unpause_image,borderwidth=0,command=pause_fnc)


back_btn.grid(row=0,column=0,padx=5)
forward_btn.grid(row=0,column=1,padx=5)
play_btn.grid(row=0,column=2,padx=5)
pause_btn.grid(row=0,column=3,padx=5)

but_frame= Frame(root)
but_frame.pack(pady=10)
add_btn=Button(but_frame,text="Add song",command=add_fnc,bg="#ffa861")
remove_btn=Button(but_frame,text="Remove song",command=rem_fnc,bg="#ff5c5c")
remove_box=Entry(but_frame,width=20,bg="#ff9696")

add_btn.grid(row=1,column=0,padx=10)
remove_btn.grid(row=1,column=1)
remove_box.grid(row=1,column=2)



root.mainloop()











