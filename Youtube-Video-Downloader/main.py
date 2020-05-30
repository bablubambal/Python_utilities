from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

# total size container:
file_size = 0


# This function call the function every second
def progress(stream=None, chunk=None,bytes_remaining=None):
    try:
        filedownloded = (file_size - bytes_remaining)
        per = (filedownloded / file_size) * 100
        dBtn.config(text="{:00.0f}% Downloaded".format(per))
    except EXCEPTION as e:
        print(e)
        print("cannot show %")


    # gets the percentage of the file that is to be downloaded


def startDownload():
    global file_size
    # to create the object of youtube video
    try:
        url = urlfield.get()
        # print(url)
        # changing Btn text
        dBtn.config(text="Please wait....")
        dBtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        # print(path_to_save-video)
        if path_to_save_video is None:
            return
        #, on_progress_callback=progress
        ob = YouTube(url, on_progress_callback=progress)
        stream = ob.streams.first()
        vTitle.config(text=stream.title)
        vTitle.pack(side=TOP)
        file_size = stream.filesize
        # print(file_size)
        stream.download(path_to_save_video)
        print("download done....")
        dBtn.config(text="Start Download")
        dBtn.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded Video Succesfully")
        urlfield.delete(0, END)
        vTitle.pack_forget()

    except EXCEPTION as e:
        print(e)
        print("Error Downloading video")


# Creating new Thread;
def startDownloadThread():
    thread = Thread(target=startDownload)
    thread.start()


# Starting the Gui window
main = Tk()
#   Setting the title
main.title("My Youtube Downloader")
# Setting icon
main.iconbitmap('icon.ico')
main.geometry("500x600")

# heading icon:
file = PhotoImage(file='youtube.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)
#text field for downloading
EnterUrl = Label(main, text="Enter the Url of Video to Download")
EnterUrl.pack(side=TOP)
# url txt field
urlfield = Entry(main, font=("verdana", 18), justify=CENTER)
urlfield.pack(side=TOP, fill=X, padx=15)

dBtn = Button(main, text="Start Download", font=("verdana", 18), relief="ridge", command=startDownloadThread)
dBtn.pack(side=TOP, pady=10)

#video title;
vTitle = Label(main,text="video Title")
# vTitle.pack(side=TOP)

Made = Label(main, text="A free Software/Program to Download the YouTube Videos\n\n Made by Bablu")
Made.pack(side=BOTTOM)
main.mainloop()
