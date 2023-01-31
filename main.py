from tkinter import *

written_text_list = [""]

def count_words():
    window.after(100, count_words)
    written_text = new_text.get("1.0",END)
    number_of_words = len(written_text.split())
    number_of_words_label.config(text=f"words {number_of_words}")

def function():
    window.after(3500, function)
    written_text = new_text.get("1.0",END)
    if written_text_list[-1] == written_text:
        new_text.delete("1.0",END)
    written_text_list.append(written_text)

window = Tk()
window.title("Do not stop writing")
window.config(padx=30,pady=30,bg="#ECF9FF")

title_label = Label(text="Do not stop typing...",bg="#ECF9FF",font=("Helvetica",50,"italic"),fg="green")
title_label.pack()

new_text = Text(bg="#20262E",fg="silver",highlightthickness=0,font=("Helvetica",13,"bold"))
new_text.focus()
new_text.pack()

number_of_words_label = Label(text="0 words",font=("Helvetica",15),bg="#ECF9FF")
number_of_words_label.pack()

count_words()
function()

window.mainloop()