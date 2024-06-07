import os
from tkinter import * 
from tkinter import Menu 
from tkinter import messagebox

def clicked1(): 
    os.startfile('Bot.py')
    btn1 = Button(window, text="Запуск бота", state= DISABLED).grid(row=2,column=0,pady=30, padx=25) 
def clicked2():
    messagebox.showinfo('Уведомление', 'Бот отключен.')
    os.system('taskkill /f /im Bot.py') 
    window.quit()

def info():
    messagebox.showinfo('Справка', 'Программа "PyTelegram Bot" разработана\nКириченко В.А. для МАОУ СОШ №20.')  

window = Tk()  
window.title("PyTelegram Bot")  
window.geometry('250x100')

btn1 = Button(window, text="Запуск бота", command=clicked1).grid(row=2,column=0,pady=30, padx=25)
btn2 = Button(window, text="Остановка бота", command=clicked2).grid(row=2,column=2,padx=5)

menu = Menu(window)
new_item = Menu(menu)
menu.add_command(label='Справка', command=info)
window.config(menu=menu)

window.mainloop()
