from tkinter import *
from pytube import YouTube

# Create the API Window
root = Tk()
root.geometry('500 * 300')  # size of the window
root.resizable(0, 0)  # makes the window adjustable with its features
root.title('Youtube Downloader')


Label(root, text="Download Youtube videos for free", font='san-serif 14 bold').pack()
link = StringVar()  # Specifying the variable type
Label(root, text="Paste your link here", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=85)

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)


root.mainloop()