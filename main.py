from pytube import YouTube
import customtkinter

# Download logic
def getVideoAndDownload(url:str) -> None:
    if url == "": 
        feedbackLabel.configure(text="Please enter a URL")
        return
    # get video
    try:
        video = YouTube(url).streams.get_highest_resolution()
    except:
        feedbackLabel.configure(text="Video not found")
        return
    # download video
    try:
        video.download()
    except:
        feedbackLabel.configure(text="Download failed")
        return
    feedbackLabel.configure(text="Video was successfully downloaded")
    urlEntry.delete(first_index=0, last_index=len(url))

# GUI
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

root = customtkinter.CTk()
root.title("YouTube to MP4")
root.geometry('500x350')

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

defaultPadding = {'pady': 12, 'padx': 10}

titleLabel = customtkinter.CTkLabel(master=frame, text="YouTube to MP4 Converter", font=('Arial', 24))
titleLabel.pack(**defaultPadding)

feedbackLabel = customtkinter.CTkLabel(master=frame, text="Paste video URL into the entry below", font=('Arial', 16))
feedbackLabel.pack(**defaultPadding)

urlEntry = customtkinter.CTkEntry(master=frame, placeholder_text="URL", width=300)
urlEntry.pack(**defaultPadding)

downloadButton = customtkinter.CTkButton(master=frame, text="Download", font=('Arial', 16), hover=True, command=lambda: getVideoAndDownload(urlEntry.get()))
downloadButton.pack(**defaultPadding)

root.mainloop()