import os
from tkinter import *
from tkinter import filedialog

import moviepy.editor
from pathlib import Path



root = Tk() # creating interface with tkinter
root.geometry("600x500")


def file(): # this command/function will makes foldier where will hold your .mp3 files and ability to choose your mp4 file
    try:
        os.mkdir(r'D:\MusicConverter') # makes foldier where will hold your converted .mp3 files

    except FileExistsError: # if file exist
        pass

    global txt
    txt2['text'] = ''
    txt.delete("1.0", 'end')
    filepath = filedialog.askopenfilename(filetypes=((('video', '*.mp4'), ('all files', '*.*') ))) # display only your .mp4 files
    txt.insert("end-1c", filepath)

def converter(): # this command/function will checking your file format and convert to .mp3
    global videofile
    try:
        if txt.get("1.0",'end-1c')[-4:] != '.mp4': # checking your file format
            txt2['text'] = 'Не тот тип файла'
            return

        videofile = Path(txt.get("1.0",'end-1c'))
        video = moviepy.editor.VideoFileClip(f'{videofile}')
        audio = video.audio # transform to .mp3
        audio.write_audiofile(f'D:\MusicConverter\{videofile.stem}.mp3') # send to your foldier which was created early
        timer()
    except:
        txt2['text'] = 'Неверный путь'

def openFoldier():
    os.startfile('D:\MusicConverter') # opens your foldier with converted .mp3 files

def timer(): # this this command/function watching file location. if downloading is over, the programm will say it
    while 1:
        try:
            os.path.isfile(f'D:\MusicConverter\{videofile.stem}.mp3') # if file exist in your foldier, it will say it
            lbl['text'] = 'Загрузка завершена'
            break

        except FileNotFoundError:
            lbl['text'] = 'Загрузка...' # when file doesn't exist in your foldier
            return timer()

################################################ making buttons, text and label widgets
txt = Text(width=45, height=1, font='Arial 12')
txt.place(x=10, y=25)

btn = Button(text='Источник', command=file, font='Arial 10')
btn.place(x=430, y=25)

btn2 = Button(text='Конвертировать', command=converter, font='Arial 10')
btn2.place(x=430, y=60)

btn3 = Button(text='Открыть папку с готовыми файлами', command=openFoldier, font='Arial 10')
btn3.pack(pady=100)

txt2 = Label(font='Arial 12 bold')
txt2.pack(pady=100)

lbl = Label(text='', font='Arial 12 bold')
lbl.pack()
#############################################

root.mainloop()
