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

        self.show_menu_bar()

        self.window.mainloop()

    def show_menu_bar(self):
        self.menu_bar = Menu(self.window)

        self.history_menu = Menu(self.menu_bar, tearoff=0)
        self.add_history(self.history_menu)

        self.menu_bar.add_cascade(label="Historique", menu=self.history_menu)
        self.menu_bar.add_command(label="Quitter", command=self.quit)

        self.window.config(menu=self.menu_bar)

    def add_history(self, menu):
        for message in self.data.get_history():
            menu.add_command(label=message)

        menu.add_separator()
        menu.add_command(label="Voir plus", command=self.show_history)
        menu.add_command(label="Tout supprimer", command=lambda: (self.data.clear_history(), self.clear_window()))

    def show_history(self):
        self.clear_window()
        self.history = self.data.get_history()
        self.history.reverse()
        self.history = self.history[:10]
        for message in self.history:
            Label(self.window, text=message).pack()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.show_menu_bar()

    def quit(self):
        self.data.save_data()
        self.window.destroy()

if __name__ == "__main__":
    app = Application("data.json")
    app.main()