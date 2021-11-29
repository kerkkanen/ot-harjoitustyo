import tkinter as tk
from ui.ui import UI


def main():

    print("Käytetäänkö tekstikäyttöliittymää,")
    print("vai tarkastellaanko tulevan graafisen liittymän ominaisuuksia?")
    while True:
        answer = input("t=teksti, g=graafinen l=lopeta\n")
        if answer == "l":
            break
        if answer == "t":
            window = tk.Tk()
            window.title("Pääkaupunkipeli")
            user_interface = UI(window)
            user_interface.txt_ui()

        if answer == "g":
            window = tk.Tk()
            window.title("Pääkaupunkipeli")
            user_interface = UI(window)
            user_interface.start()
            window.mainloop()

    print("Heippa!")


if __name__ == '__main__':
    main()
