from ui import UI
import tkinter as tk

def main():    
    window = tk.Tk()
    window.title("Pääkaupunkipeli")

    ui = UI(window)   
    ui.start()

    window.mainloop()
   


if __name__ == '__main__':
    main()