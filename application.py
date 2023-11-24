from tkinter import Tk, Menu, Frame, Text, Button, Label, END
from tkinter import messagebox
from tkinter import ttk
from data import Data
from request import Request
import threading

class Application:
    WIDTH = 1024
    HEIGHT = 768

    def __init__(self, name_data):
        self.data = Data(name_data)
        self.data.load_data()
        self.request = Request(self.data)
        self.current_history = 0

    def main(self):
        self.window = Tk()
        self.window.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.window.title("Application")

        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#ccc")

        self.show_menu_bar()
        self.show_main()

        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
        self.window.mainloop()

    def on_close(self):
        if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter?"):
            self.data.save_data()
            self.window.destroy()

    def show_menu_bar(self):
        self.menu_bar = Menu(self.window)

        self.history_menu = Menu(self.menu_bar, tearoff=0)
        self.add_history(self.history_menu)

        self.menu_bar.add_cascade(label="Historique", menu=self.history_menu)
        self.menu_bar.add_command(label="Quitter", command=self.on_close)

        self.window.config(menu=self.menu_bar)

    def add_history(self, menu):
        self.history = self.data.get_history()
        self.history.reverse()
        for message in self.history[:10]:
            menu.add_command(label=self.shorten_message(message[0]), command=lambda message=message: self.show_result(message[0], message[1]))

        menu.add_separator()
        menu.add_command(label="Voir plus", command=self.show_history)
        menu.add_command(label="Tout supprimer", command=lambda: (self.data.clear_history(), self.clear_window()))

    def shorten_message(self, message):
        if len(message) >= 7:
            message = message[:7] + "..."
        print(message)
        return message
    
    def show_history(self):
        self.clear_window()
        self.history_frame = Frame(self.window)
        self.history = self.data.get_history()
        for index, message in enumerate(self.history):
            ttk.Label(self.history_frame, text=message[0]).grid(row=index, column=0, pady=5, padx=5)
            ttk.Button(self.history_frame, text="X", command=lambda index=index: self.delete_history(index)).grid(row=index, column=1, pady=5)

        self.history_frame.pack()

    def show_main(self):
        self.clear_window()
        self.main_frame = Frame(self.window)    
        self.main_frame.pack()

        ttk.Label(self.main_frame, text="Entrez votre message :").pack(pady=10)

        self.result_text = Text(self.main_frame, height=4, width=60)
        self.result_text.pack(expand=True, pady=10)

        ttk.Button(self.main_frame, text="Envoyer", command=lambda: threading.Thread(target=self.send_message).start()).pack()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.show_menu_bar()

    def delete_history(self, index):
        self.data.delete_history(index)
        self.clear_window()
        self.show_history()

    def send_message(self):
        message = self.result_text.get("1.0", END)
        result = self.request.get(message)

        self.data.add_history(message, result)

        self.show_result(message, result)

    def show_result(self, message, result):
        self.clear_window()

        self.result_frame = Frame(self.window)
        self.result_frame.pack()

        self.message = Text(self.result_frame, height=4, width=60)
        self.message.insert(END, message)
        self.message.pack(pady=10)

        ttk.Label(self.result_frame, text=result[0]["generated_text"]).pack(pady=10)

        ttk.Button(self.result_frame, text="Relancer le prompt", command=lambda: threading.Thread(target=self.relaunch_prompt, args=(message,)).start()).pack(pady=5)
        ttk.Button(self.result_frame, text="Retour", command=self.show_main).pack(pady=5)

    def relaunch_prompt(self, message):
        self.data.delete_history_message(message)

        message = self.message.get("1.0", END)
        result = self.request.get(message)

        self.data.add_history(message, result)

        self.show_result(message, result)

if __name__ == "__main__":
    app = Application("data.json")
    app.main()
