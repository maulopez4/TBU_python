import tkinter as tk
from tkinter import StringVar, Toplevel, ttk
from tkinter.constants import CENTER, E, GROOVE, NSEW, NW, SW, W
from tkinter import messagebox
import pymysql
from python_mysql_dbconfig import read_db_config
from db_lib import MySQLDataBase
import sys
import uuid
import TBU_main
import subprocess

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit(12**3)

class App(tk.Tk):
    def __init__(self):
        self.welcome_window=tk.Tk()
        
        self.welcome_window.geometry("335x160")
        self.welcome_window.resizable(0, 0)
        self.welcome_window.title("TBU Login")
        self.welcome_window.iconbitmap("resources\\tbu-icon.ico")

        # configure style
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Segoe', 10, 'bold'))
        self.style.configure('TButton', font=('Segoe', 10, 'bold'))

        #LabelFrame
        self.login_labelframe=ttk.LabelFrame(self.welcome_window, text="")        
        self.login_labelframe.grid(column=0, row=0, padx=5, pady=1)
        self.login_labelframe.columnconfigure(0, weight=2)
        self.login_labelframe.columnconfigure(1, weight=1)
        self.login_labelframe.columnconfigure(2, weight=1)
        self.login_labelframe.rowconfigure(0, weight=1)
        self.login_labelframe.rowconfigure(1, weight=1)
        self.login_labelframe.rowconfigure(2, weight=1)
        self.login_entry()
        #Frame
        self.button_frame=ttk.Frame(self.welcome_window)        
        self.button_frame.grid(column=0, row=1, padx=0, pady=1)
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=1)        
        self.login_buttons()

        self.welcome_window.mainloop()

    def login_entry(self):
        
        global username_verification
        global password_verification

        username_verification=StringVar()
        password_verification=StringVar()

        global username_entry
        global password_entry
 
        self.welcome_logo=tk.PhotoImage(file='resources\\leer-logo.png')
        self.welcome_logo=self.welcome_logo.subsample(2,2)
        self.welcome_label=ttk.Label(self.login_labelframe, image=self.welcome_logo)
        self.welcome_label.grid(column=0, row=0, rowspan=2, padx=0, pady=0, sticky=NSEW)
        self.login_label=ttk.Label(self.login_labelframe, text="User Name:")
        self.login_label.grid(column=1, row=0, padx=4, pady=4, sticky=SW)
        self.username_entry=ttk.Entry(self.login_labelframe, textvariable=username_verification)
        self.username_entry.grid(column=2, row=0, padx=4, pady=4, sticky=SW)
        self.password_label=ttk.Label(self.login_labelframe, text="Password:")        
        self.password_label.grid(column=1, row=1, padx=4, pady=4, sticky=NW)
        self.password_entry=ttk.Entry(self.login_labelframe, show="*", textvariable=password_verification)
        self.password_entry.grid(column=2, row=1, padx=4, pady=4, sticky=NW)
        
    def login_buttons(self):    
        self.login_boton=ttk.Button(self.button_frame, text="Login", command= self.login_window)
        self.login_boton.grid(column=0, row=0, padx=4, pady=4, sticky=W)
        self.cancel_button=ttk.Button(self.button_frame, text="Cancel", command= self.close_window)
        self.cancel_button.grid(column=1, row=0, padx=4, pady=4, sticky=W)

    def login_window(self):
        global data_validation
        user=(str(username_verification.get()))
        passwd=(str(password_verification.get()))
        h=(user,passwd)
        y=("SELECT * from users_tbl WHERE users_username=%s AND users_password=%s")
        conn = MySQLDataBase().connection(read_db_config())
        cursor = conn.cursor()
        cursor.execute(y,h)
        
        if cursor.fetchall():
            messagebox.showinfo("Success","Login Successful")
            #my_id = uuid.uuid1() # or uuid.uuid4()
            subprocess.call("TBU_main.py", shell=True)
        else:
            messagebox.showinfo("Failed", "Login Failed") 
            self.username_entry.delete(0,'end')
            self.password_entry.delete(0,'end')
            self.username_entry.focus()

        cursor.close()
        conn.close()    

    def close_window(self):
       global close_window
       self.welcome_window.destroy()            

if __name__ == "__main__":
    app = App()
    app.mainloop()
