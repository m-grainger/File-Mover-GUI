
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import time, os, shutil


class Feedback:

    def __init__(self, master):

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        master.geometry('600x200') 
        master.title('File Mover')
        master.resizable(False,False)
       
        ttk.Label(self.frame_header, text = 'Welcome to the File Moving Program!').grid(row = 0, column = 0, rowspan = 3, pady = 10)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        self.sourceName = StringVar()
        self.sourceName.set("Select Source")

        self.destName= StringVar()
        self.destName.set("Select Destination")
        
        ttk.Label(self.frame_content, text ='Click on the button to the right to'
                  ' choose the folder to check.').grid(row = 1, column = 0, rowspan = 2, pady = 5, padx = 5, sticky = W)
        
        ttk.Label(self.frame_content, textvariable = self.sourceName).grid(row = 2, column = 0, rowspan = 3, pady = 5, padx = 5, sticky = W)
        
        ttk.Label(self.frame_content, text ='Click on the button to the right to'
                  ' set the destination folder for your files.').grid(row = 3, column = 0, rowspan = 2, pady = 5, padx = 5, sticky = W)
        
        ttk.Label(self.frame_content, textvariable = self.destName).grid(row = 4, column = 0, rowspan = 3, pady = 10, padx = 5, sticky = W)

        ttk.Label(self.frame_content, text ='Click on the button to the right to move files to the destination folder that \nare less than 24 hours old, '
                  'or that have been edited within'
                  ' the last 24 hours.').grid(row = 5, column = 0, rowspan = 2, pady = 5, padx = 5, sticky = W)

        ttk.Button(self.frame_content, text = 'Select Source'
                   ' Folder', command = lambda: file_src(self)).grid(row = 2, column = 6, pady = 5, ipadx = 3, ipady = 3, padx = 5, sticky = E)
        ttk.Button(self.frame_content, text = 'Select'
                   ' Destination', command = lambda: file_dest(self)).grid(row = 4, column = 6, pady = 10, padx = 6, ipady = 3, ipadx = 8, sticky = E)
        ttk.Button(self.frame_content, text = 'Click Here'
                   ' to Execute', command = lambda: execute_func(self)).grid(row = 5, column = 6, pady = 25, padx = 5, ipady= 3, sticky = E)


  
def main():
    root = Tk()
    feedback = Feedback(root)
    
def file_src(self):

    dirname = filedialog.askdirectory()
    self.sourceName.set(dirname)
    if dirname:
        print(dirname)

def file_dest(self):
    dirname = filedialog.askdirectory()
    self.destName.set(dirname)
    if dirname:
        print(dirname)

def execute_func(self):
    folder_src = self.sourceName.get()
    folder_dest = self.destName.get()
    filecopy(self, folder_src, folder_dest)

def filecopy(self, file_src, file_dest):
    now = time.time() 
    docs = os.listdir(file_src)
    for i in docs:
        file_name = file_src + '\\' + i 
        new_or_edited = os.stat(file_name).st_mtime 
        one_day = (now - 86400)  
        if new_or_edited > one_day:  
            shutil.copy(file_name, file_dest) 
            print('Program executed')

        
if __name__ == "__main__":
    main() 

  
