import tkinter as tk
from pytube import YouTube

def download_video():
    link = vidoe_link.get()
    try:
        YouTube(link).streams.first().download(r'C:\Users\HP\Desktop\YT video')
        done_heading.config(text='Your video is downloaded at : Desktop/Yt Videos')
    except:
        done_heading.config(text="Sorry :(we can't download this video)")

root = tk.Tk()
root.title('YouTube Downloader')
root.geometry('1000x600')
root.config(bg='#FCF5E5')

heading= tk.Label(text='YouTube Downloader',font=('Harlow Solid Italic ',60),bg='#FCF5E5',fg='#CE0601')
heading.pack(pady=20)

sub_heading = tk.Label(text='Paste your link here....',font=('Harlow Solid Italic ',30),fg='#B7B9AF',bg='#FCF5E5')
sub_heading.pack(pady=20)

vidoe_link =tk.Entry(font=('Bahnschrift Light Condensed',20),width=60,bg='#B7B9AF')
vidoe_link.pack()

btn = tk.Button(text='Download',font=('Harlow Solid Italic',20),relief='groove',bg='#4e5454',width=22,fg='White'
                ,command=download_video)
btn.pack(pady=20)

done_heading = tk.Label(text='',font=('Harlow Solid Italic ',30),fg='#FCF5E5',bg='#FCF5E5')
sub_heading.pack(pady=20)


root.mainloop()