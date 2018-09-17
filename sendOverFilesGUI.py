from tkinter import Tk, Label, Button, Entry, Text, Scrollbar, END
from tkinter.scrolledtext import ScrolledText 
from tkinter.messagebox import showinfo
from sendOverFiles import transmission
class GUI():
    __server = transmission()

    def reFresh(self):
        print("in")
        #self.showChat.delete('1.0', END)
        self.showChat.insert(END, self.__server.readingLog() )
        self.root.after(1000, self.reFresh)

    def sendMessage(self, event=None):
        self.__server.writingLog(self.userInput.get())
        self.userInput.delete(first = 0, last=len(self.userInput.get()))

    def __init__(self):


        self.root = Tk()
        
        #self.text = Label(
        #    self.root,
        #    text = "Enter text: "
        #)
        self.showChat = ScrolledText(self.root, width=30, height = 15 )
        #self.temp = self.dataInput.get(index1=1.0, index2=END)
        self.userInput = Entry(self.root)
        #self.temp = self.dataInput.get(index1=1.0, index2=END)
        #self.execButton = Button(
        #    self.root,
        #    text = "Encrypt",
        #    command = self.pushString
        #    #background = "green"
        #)
        self.sendButton = Button(
            self.root,
            text = "Send",
            command = lambda: self.sendMessage()
            #background = "green"
        )
        self.showChat.grid(
            row = 1,
            column = 1,
            columnspan = 7,
            pady = 10,
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
