"import tkinter
import customtkinter
from pytube import YouTube
from pytubefix import YouTube
text_g = ""
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def startDownload():
    try:

        ytLink = url.get()
        ytDown = YouTube(ytLink)
        video = ytDown.streams.get_highest_resolution()
        video.download()
        print("Download Complate")
        text_g =  ytDown.title
        title2 = customtkinter.CTkLabel(app, text="-"+text_g+"-"+" Judicial video was uploaded with success!")
        title2.pack()


    except:
        print("Youtube Link is Invalide. Try Again")



app = customtkinter.CTk()
app.geometry("720x480")
app.title("Sevim's Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Instert The Youtube URL")
title.place(relx=0.4,rely=0.15,relwidth=0.2)

main = customtkinter.CTkFrame(app)
main.place(relx=0.20,rely=0.25,relwidth=0.7,relheight=0.08)

url = customtkinter.CTkEntry(main,placeholder_text="Paste Link Here...",font=("Helvetica", 14), state="normal",corner_radius=0,border_width=0)
url.place(relx=0,rely=0.,relwidth=1,relheight=1)

button = customtkinter.CTkButton(url,text="Start",hover_color="blue", command=startDownload)
button.place(relx=0.75,rely=0.1,relwidth=0.23,relheight=0.8)





app.mainloop()"