import tkinter as tk
from tkinter import ttk
from tkinter.constants import CENTER, E, GROOVE, NSEW, NW, SW, W
from tkinter import messagebox
import pymysql
from python_mysql_dbconfig import read_db_config
from db_lib import MySQLDataBase
import sys
import uuid
 
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit(10**4)

class App(tk.Tk):
    def __init__(self):
        self.main_window=tk.Tk()
        self.main_window.geometry("640x480")
        self.main_window.resizable(0, 0)
        self.main_window.title("TBU Main")
        self.main_window.iconbitmap("resources\\tbu-icon.ico")

        # configure style
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Segoe', 10, 'bold'))
        self.style.configure('TButton', font=('Segoe', 10, 'bold'))

        #LabelFrame
        self.userbutton_frame=ttk.Labelframe(self.main_window, text="User Options")       
        self.userbutton_frame.grid(column=0, row=0, padx=5, pady=1, sticky=W)
        self.userbutton_frame.columnconfigure(0, weight=2)
        self.userbutton_frame.columnconfigure(1, weight=1)
        self.userbutton_frame.columnconfigure(2, weight=1)
        self.userbutton_frame.rowconfigure(0, weight=1)
        self.userbutton_frame.rowconfigure(1, weight=1)
        self.userbutton_frame.rowconfigure(2, weight=1)       
        self.user_buttons()

        self.superbutton_frame=ttk.Labelframe(self.main_window, text="Supervisor Options")       
        self.superbutton_frame.grid(column=0, row=1, padx=5, pady=1, sticky=W)
        self.superbutton_frame.columnconfigure(0, weight=2)
        self.superbutton_frame.columnconfigure(1, weight=1)
        self.superbutton_frame.columnconfigure(2, weight=1)
        self.superbutton_frame.rowconfigure(0, weight=1)
        self.superbutton_frame.rowconfigure(1, weight=1)
        self.superbutton_frame.rowconfigure(2, weight=1)       
        self.super_buttons()

        self.adminbutton_frame=ttk.Labelframe(self.main_window, text="Admin Options")       
        self.adminbutton_frame.grid(column=0, row=2, padx=5, pady=1, sticky=W)
        self.adminbutton_frame.columnconfigure(0, weight=2)
        self.adminbutton_frame.columnconfigure(1, weight=1)
        self.adminbutton_frame.columnconfigure(2, weight=1)
        self.adminbutton_frame.rowconfigure(0, weight=1)
        self.adminbutton_frame.rowconfigure(1, weight=1)
        self.adminbutton_frame.rowconfigure(2, weight=1)       
        self.admin_buttons()

        self.main_window.mainloop()

    def user_buttons(self):
        self.newentry_boton=ttk.Button(self.userbutton_frame, text="New Entry")
        self.newentry_boton.grid(column=0, row=0, padx=4, pady=4, sticky=W)
        self.inspectentry_button=ttk.Button(self.userbutton_frame, text="Inspect Entry")
        self.inspectentry_button.grid(column=1, row=0, padx=4, pady=4, sticky=W)
        self.searchentry_button=ttk.Button(self.userbutton_frame, text="Search Entry")
        self.searchentry_button.grid(column=2, row=0, padx=4, pady=4, sticky=W)

    def super_buttons(self):
        self.newentry_boton=ttk.Button(self.superbutton_frame, text="Add/Edit Entry")
        self.newentry_boton.grid(column=0, row=0, padx=4, pady=4, sticky=W)
        self.inspectentry_button=ttk.Button(self.superbutton_frame, text="Add/Edit Mold")
        self.inspectentry_button.grid(column=1, row=0, padx=4, pady=4, sticky=W)
        self.searchentry_button=ttk.Button(self.superbutton_frame, text="Add/Edit Paintcode")
        self.searchentry_button.grid(column=2, row=0, padx=4, pady=4, sticky=W) 

    def admin_buttons(self):
        self.newentry_boton=ttk.Button(self.adminbutton_frame, text="Add/Edit User")
        self.newentry_boton.grid(column=0, row=0, padx=4, pady=4, sticky=W)
         

    #def close_window(self):
    #   global close_window
    #   self.main_window.destroy()            

if __name__ == "__main__":
    app = App()
    app.mainloop()        