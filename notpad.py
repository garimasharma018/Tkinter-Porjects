import tkinter as tk
from tkinter import filedialog


class notepad():
    def __init__(self,root):
        self.file_path= None
        self.root = root
        root.title('Notepad')
        root.geometry('800x650')
        root.config(bg='#00CED1')

        heading =tk.Label(text=('Notepad'),font=('Brush Script MT',30),
                                                fg='yellow',bg='#00CED1')
        heading.place(x=340,y=10)

        btn1= tk.Button(text='Open',font=('Bahnschrift SemiBold SemiConden',30),
                    bg='yellow',fg='white',relief='solid',command=self.open_file)
        btn1.place(x=10,y=80)

        btn2= tk.Button(text='Save',font=('Bahnschrift SemiBold SemiConden',30),
                    bg='red',fg='white',relief='solid',command=self.save)
        btn2.place(x=160,y=80)


        btn3= tk.Button(text='Save As',font=('Bahnschrift SemiBold SemiConden',30),
                    bg='gray',fg='white',relief='solid',command=self.save_as)
        btn3.place(x=310,y=80)


        btn4= tk.Button(text='Clear',font=('Bahnschrift SemiBold SemiConden',30),
                    bg='pink',fg='white',relief='solid',command=self.clear)
        btn4.place(x=520,y=80)

        btn5= tk.Button(text='Help',font=('Bahnschrift SemiBold SemiConden',30),
                    bg='orange',fg='white',relief='solid',command=self.help)
        btn5.place(x=670,y=80)

        self.text_area = tk.Text(font=('Bahnschrift SemiBold SemiConden',15),width=77,height=17,relief='solid')
        self.text_area.place(x=10,y=170)
    
    def open_file(self):
        self.clear()
        self.file_path = filedialog.askopenfilename()
        with open(self.file_path,'r') as notepad_file:
            text = notepad_file.read()
        self.text_area.insert(0.0,text)
        self.root.title(f'notepad:{self.file_path}')

    def save(self):
        if self.file_path:
            text = self.text_area.get(0.0,tk.END)
            with open(self.file_path,'w') as notepad_file:
              notepad_file.write(text)
        else:
            self.save_as()


    def save_as(self):
           text = self.text_area.get(0.0,tk.END)
           lst = [("Python (.py)",'*.py'),('Text(.txt)','*.txt'),('Bat(.bat)','*.bat'),('All Types','*,*')]
           file_path = filedialog.asksaveasfilename(defaultextension='.txt',filetype=lst)
           with open(file_path,'w') as notepad_file:
            notepad_file.write(text)



    def clear(self):
        self.text_area.delete(0.0,tk.END)

    def help(self):
        help_text = '''
Notepad is a basic text editor that is included with Windows.
It is a simple program that can be used to create and 
edit text files. Notepad is not a word processor, so it does not have
many of the features that are found in word processors, such as the 
ability to create and edit tables, images, or charts. 
However, Notepad is a great tool for creating simple text files, 
such as program code, scripts, or notes.

To use Notepad, simply open the program and start typing.
 You can use the keyboard to type in text, and you can use 
the mouse to select text and perform other actions.
 Notepad does not have a lot of menus or buttons, so it is very 
easy to learn how to use.

When you are finished editing a text file, you can save it by clicking
on the "File" menu and selecting "Save." You will be prompted to enter a
filename and location for the file. Notepad will save the file as a 
plain text file with a .txt extension.

Here are some of the things you can do with Notepad:

Create and edit text files
Save text files in a variety of formats
Search for text within a text file
Replace text within a text file
Use keyboard shortcuts to perform common tasks
Print text files
Notepad is a very versatile tool that can be used for a variety of tasks.
It is a great tool for beginners and experienced 
users alike.

Here are some additional tips for using Notepad:

    # o select a block of text, hold down the left mouse button and
     drag the mouse over the text you want to select.
    # To copy selected text, press the "Ctrl" key and
     the "C" key at the same time.
    # To paste copied text, press the "Ctrl" key and
     the "V" key at the same time.
    # To search for text within a text file, click on the "Edit" menu
     and select "Find." Enter the text you want to search for and 
    # click on the "Find Next" button.
    # To replace text within a text file, click on the "Edit" menu and
     select "Replace." Enter the text you want to replace and the 
    # text you want to replace it with. Click on the "Replace" button
     to replace the first occurrence of the text, or click on the 
    # "Replace All" button to replace all occurrences of the text.
    # To use keyboard shortcuts to perform common tasks, click on the 
    "Help" menu and select "Keyboard shortcuts."
        

'''
        self.clear()
        self.text_area.insert(0.0,help_text)
    
    



window = tk.Tk()

notepad = notepad(window)


window.mainloop()
