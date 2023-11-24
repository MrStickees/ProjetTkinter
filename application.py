from tkinter import *
from data import Data

class Application:
    def __init__(self, name_data):
        self.data = Data(name_data)
        self.data.load_data()
        print(self.data)

    def main(self):
        self.window = Tk()
        self.window.geometry("500x500")
        self.window.title("Application")

        self.showMenuBar()

        self.window.mainloop()

    def showMenuBar(self):
        self.menu_bar = Menu(self.window)

        self.history_menu = Menu(self.menu_bar, tearoff=0)
        self.history_menu.add_command(label="Quit", command=self.quit)
        self.history_menu.add_separator()

        self.addHistory(self.history_menu)
        self.menu_bar.add_cascade(label="History", menu=self.history_menu)


        
        self.window.config(menu=self.menu_bar)
    def addHistory(self, menu):
        for message in self.data.get_history():
            menu.add_command(label=message)

        
        


    def quit(self):
        self.data.save()
        self.window.destroy()


if __name__ == "__main__":
    app = Application("private/data.json")
    app.main()