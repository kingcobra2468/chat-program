from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, END, Menu, Toplevel
from tkinter.scrolledtext import ScrolledText 
from tkinter.messagebox import showinfo
from sendOverFiles import transmission
import time

class GUI():
    __server = transmission()
    __isOn = False
    __name = "Anonymous"

    def autoScroll(self):
        self.__isOn = False if self.__isOn else True

    def pullName(self, event = None):
        self.__name = str(self.name.get())
        self.name.delete(
            first = 0,
            last = len(self.name.get())
        )
        self.window.destroy()
    def nameInput(self):
        self.window = Toplevel(self.root)
        self.name = Entry(
            self.window,
        )
        self.nameLabel = Label(
            self.window,
            text = "Name",
            padx = 10,
            pady = 10
        )
        self.name.focus_set()
        self.nameLabel.pack(side = "top")
        self.name.pack(side = "bottom")
        
        self.window.bind('<Return>', self.pullName)
        #window.destroy()

    def reFresh(self):
        print("in")
        #self.showChat.delete('1.0', END)
        self.showChat.config(state = 'normal')
        self.showChat.insert(END, self.__server.readingLog())
        self.showChat.config(state = 'disabled')
        if self.__isOn:
            self.showChat.see('end')
        self.root.after(1000, self.reFresh)

    def sendMessage(self, event=None):
        self.__server.writingLog(self.userInput.get(), self.__name)
        self.userInput.delete(first = 0, 
            last=len(self.userInput.get()))

    def __init__(self):

        self.root = Tk()
        self.nameInput()
        self.menuBar = Menu(
            self.root,
            activebackground = "orange2",
            bg = "orange2",
            tearoff = 0
        )

        self.showChat = ScrolledText(
            self.root,
            width=30,
            height = 15, 
            state = 'normal')

        self.userInput = Entry(self.root)

        self.sendButton = Button(
            self.root,
            text = "Send",
            command = lambda: self.sendMessage(),
            background = "orange2"
        )

        self.userInput.focus_set()

        self.showChat.grid(
            row = 1,
            column = 1,
            columnspan = 7,
            pady = 5,
            padx = 10
        )
        self.userInput.grid(
            row = 2,
            column = 1,
            columnspan = 2,
            pady = 10,
            padx = 10
        )
        self.sendButton.grid(
            row = 2,
            column = 7,
            pady = 10,
            padx = 10
        )

        #self.root.geometry("800x800")
        #https://www.tutorialspoint.com/python3/tk_menu.htm
        #self.menuBar.config(width = 3)

        self.root.config(menu=self.menuBar)
        self.options = Menu(
            self.menuBar, 
            tearoff = 0)
        self.menuBar.add_cascade(
            label='Options', 
            menu = self.options)
        #options.add_command(label = 'Scroll-Lock')
        self.options.add_checkbutton(
            label = 'Auto-Scroll', 
            command = self.autoScroll, 
            background = "grey", 
            activebackground = "grey", 
            selectcolor = "white", 
            onvalue=True, 
            offvalue=False,
            variable = self.__isOn
            )
        self.options.add_command(
            label = 'Name', 
            command = self.nameInput, 
            background = "grey", 
            #activebackground = "grey", 
            #selectcolor = "white", 
            )

        self.root.after(1000, self.reFresh)
        self.root.title('Erik Tyryshkin Chat Program')
        self.root.configure(bg='grey')
        self.root.bind('<Return>', self.sendMessage)
        self.root.mainloop()
        
     
#label = tkinter.Label(master = top, text = "Hello World") 
#label.grid(row=1, column = 2, columnspan = 1)
#label1 = tkinter.Label(master = top, text = "ZZZZZZZZZ") 
#label1.grid(row=2, column = 7, columnspan = 10)
#def test():
#    print("PEOP")
#top.config(bg = "black")
#button = tkinter.Button( self.root , text = "Click here", command = test )
#button.pack()
test = GUI()
