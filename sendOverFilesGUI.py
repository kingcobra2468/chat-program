from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, END, Menu
from tkinter.scrolledtext import ScrolledText 
from tkinter.messagebox import showinfo
from sendOverFiles import transmission
class GUI():
    __server = transmission()

    def reFresh(self):
        print("in")
        #self.showChat.delete('1.0', END)
        self.showChat.config(state = 'normal')
        self.showChat.insert(END, self.__server.readingLog())
        self.showChat.config(state = 'disabled')
        self.showChat.see('end')
        self.root.after(1000, self.reFresh)

    def sendMessage(self, event=None):
        self.__server.writingLog(self.userInput.get())
        self.userInput.delete(first = 0, 
            last=len(self.userInput.get()))

    def __init__(self):

        self.root = Tk()

        self.menuBar = Menu(
            self.root,
            activebackground = "orange2",
            bg = "orange2",
            tearoff = 0
        )
        self.menuBar
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
            row =2,
            column = 7,
            pady = 10,
            padx = 10
        )

        #self.root.geometry("800x800")
        #https://www.tutorialspoint.com/python3/tk_menu.htm
        #self.menuBar.config(width = 3)
        self.root.config(menu=self.menuBar)
        options = Menu(self.menuBar)
        self.menuBar.add_cascade(label='Options', menu = options)
        options.add_command(label = 'Scroll-Lock')

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
