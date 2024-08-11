# BetterDownloads alpha is a simple application made in Python that organizes all the files in one directory and copies/moves them to another.
The idea behind the project lies within the downloads folder. I've been using my desktop PC for several years now and when I looked through my _/Downloads_ folder, I noticed that it is practically impossible to find something specific if I don't remember the name or date of the file.
BetterDownloads organizes files by their extensions. It creates folders such as **"Videos"**, **"Documents"**, **"Presentations"**, **"Applications"** etc. that make it much easier to find anything you need.
![image](https://github.com/user-attachments/assets/2ee67002-25df-45d4-9ee2-99b9f48357c2)

If your directory has folders, the app will copy them completely, and if it finds rare or obscure extensions, files will be moved to **"Other"**.
At first, the app was programmed to deal with the Windows */Downloads* folder, but it is possible to choose any start and end folder on the PC.

![image](https://github.com/user-attachments/assets/c141d8e4-fbb8-400a-946d-35f91e1ace10)

This is an example of an end result.

The application has two Python files, **logic.py** and **main_gui.py**. GUI is done using _Tkinter_, and copying is done via _Shutil_.
