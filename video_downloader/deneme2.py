import tkinter
import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk
import io
import requests

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def startDownload():
    try:
        ytLink = url.get()
        ytDown = YouTube(ytLink)
        
        # Get the highest resolution stream
        video = ytDown.streams.get_highest_resolution() 
        video.download()
        
        print("Download Complete")

        # Get the thumbnail URL and display it
        thumbnail_url = ytDown.thumbnail_url
        response = requests.get(thumbnail_url)
        response.raise_for_status()  # Will raise HTTPError for bad responses
        img_data = response.content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((200, 200), Image.ANTIALIAS)  # Resize if necessary
        img_tk = ImageTk.PhotoImage(img)

        # Update the label with the new image
        thumbnail_label.config(image=img_tk)
        thumbnail_label.image = img_tk

    except requests.RequestException as e:
        print(f"Network error: {e}")
        thumbnail_label.config(text="Failed to fetch thumbnail")

    except Exception as e:
        print(f"Error: {e}")
        print("Youtube Link is Invalid or Other Error. Try Again")
        thumbnail_label.configure(text="Error loading video")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Sevim's Youtube Downloader")

title = customtkinter.CTkLabel(app, text="Insert The Youtube URL")
title.place(relx=0.4, rely=0.15, relwidth=0.2)

url_var = tkinter.StringVar()
url = customtkinter.CTkEntry(app, width=500, textvariable=url_var)
url.place(relx=0.25, rely=0.25, relwidth=0.5)

button = customtkinter.CTkButton(app, text="Start", command=startDownload)
button.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.06)

# Create a label to display the thumbnail
thumbnail_label = customtkinter.CTkLabel(app)
thumbnail_label.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.2)

app.mainloop()
