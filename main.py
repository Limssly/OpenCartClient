import tkinter as tk

def say_hello():
    print("Hello, Tkinter!")

root = tk.Tk()
root.title("Monitoring Application")

button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack()

root.mainloop()
