import tkinter as tk
from ui.ui import UI


def main():

    window = tk.Tk()
    window.title("Pääkaupunkipeli")
    user_interface = UI(window)
    user_interface.start()
    window.mainloop()


if __name__ == '__main__':
    main()
