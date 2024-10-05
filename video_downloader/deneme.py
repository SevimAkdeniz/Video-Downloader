import tkinter
import customtkinter
from pytube import YouTube
from pytubefix import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def show():
    try:
        link = url.get()
        ytlink = YouTube(link)
        video = ytlink.title
        print(video)



    except:
        print("Youtube Link is Invalide. Try Again")


app = customtkinter.CTk()
app.geometry("720x480")
app.title("Sevim's Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Instert The Youtube URL")
title.place(relx=0.4,rely=0.15,relwidth=0.2)

main = customtkinter.CTkFrame(app)
main.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.08)

url = customtkinter.CTkEntry(main,placeholder_text="Paste Link Here...",font=("Helvetica", 14), state="normal",corner_radius=0,border_width=0)
url.place(relx=0,rely=0.,relwidth=1,relheight=1)

button = customtkinter.CTkButton(url,text="Start",hover_color="blue", command=show)
button.place(relx=0.75,rely=0.1,relwidth=0.23,relheight=0.8)


title2 = customtkinter.CTkLabel(app, text="Judicial video was uploaded with success!")
title2.place(relx=0.08,rely=0.4,relwidth=0.9) 


app.mainloop()