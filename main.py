# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
import webbrowser
import time
import pyperclip
import pyautogui
from pywinauto import Application, keyboard


root = tk.Tk()
root.title("Desktop App")


def open_website():
    webbrowser.open_new_tab("https://zakupki.gov.ru/epz/main/public/home.html")
    time.sleep(10)  # Wait for the website to load









def login_terminal():
    app_location = (26, 28)
    pyautogui.moveTo(app_location)
    pyautogui.doubleClick(app_location)
    time.sleep(2)
    # Move the mouse and click on the password field
    password_field_location = (904, 791)
    pyautogui.moveTo(password_field_location)
    pyautogui.click()
    time.sleep(2)

    password = 'OLGA1234'
    pyperclip.copy(password)
    time.sleep(0.5)
    pyautogui.typewrite(password)

    # Press Enter to submit the login form
    enter_location = (857, 798)
    pyautogui.moveTo(enter_location)
    pyautogui.click(enter_location)


def handle_button_press():

    login_terminal()



def handle_button_press2():
    open_website()


# Start Sirena Button
start_sirena_btn = tk.Button(root, text="Запуск сирены", command=handle_button_press)
start_sirena_btn.pack()

zakupki_start_btn = tk.Button(root, text="Запуск сайта тендеров", command=handle_button_press2)
zakupki_start_btn.pack()


root.mainloop()
