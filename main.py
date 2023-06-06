from tkinter import END
from tkinter.scrolledtext import ScrolledText
import test


# from test import *
try:
    import Tkinter as tk
except:
    import tkinter as tk

import prettytable
import tkinter.messagebox
from pygame import mixer
import sqlite3
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import argparse
import imutils
import time
from datetime import date
import datetime
import dlib
import cv2
import os
import smtplib
import customtkinter
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from tkinter import ttk
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

# uid = 0



def hel():
    help(cv2)


def Contri():
    tkinter.messagebox.showinfo(
        "Contributor", "\n1. Bethlehem Tassew")


def anotherWin():
    tkinter.messagebox.showinfo(
        "About", 'Driver Drowsiness Detection System version')


class SampleApp(tk.Tk):

    def __init__(self):

        # root.geometry('500x570')
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title("Driver Drowsiness Detection System")
        menu = tk.Menu(self)
        self.config(menu=menu)
        subm1 = tk.Menu(menu)
        menu.add_cascade(label="Tools", menu=subm1)
        subm1.add_command(label="Open CV Docs", command=hel)
        subm2 = tk.Menu(menu)
        menu.add_cascade(label="About", menu=subm2)
        subm2.add_command(label="DDDS", command=anotherWin)
        subm2.add_command(label="Contributors", command=Contri)

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        # new_frame.config(self,relief="ridge",borderwidth=2)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=1)





class StartPage(tk.Frame):

    def __init__(self, master):

        def dbcheck():

            password = Password.get()
            uname = UserName.get()
            conn = sqlite3.connect('data.db')
            global uid
            cursor = conn.cursor()
            cursor.execute(
                'SELECT EXISTS(SELECT * FROM Users where UserName=? AND Password=?)', (uname, password))
            row = cursor.fetchone()
            # conn.commit()

            
            if row[0]:
                # row=cursor.fetchone()
                uid = uname

                print("Welcome\n ID:" + uid)
                master.switch_frame(PageTwo)
            else:
                print("Login Failed")
                tkinter.messagebox.showinfo(
                    "Login Error", "Wrong username or password")

        tk.Frame.__init__(self, master)
        filename = tk.PhotoImage(file="background.jpeg")

        tk.Frame.config(self, relief="ridge", borderwidth=2,
                        background='black')

        tk.Label(self, text="DRIVER\n DROWSINESS\n DETECTION SYSTEM\n", font=(
            'Times 35 bold'), background='black').pack(side="top")


        l = tk.Label(self, image=filename)
        l.img = filename

        l.pack()
        UserName = tk.StringVar()
        Password = tk.StringVar()

        label_1 = tk.Label(self, text="User Name", width=20, font=("bold", 10))
        label_1.place(x=80, y=280)
        entry_1 = tk.Entry(self, textvar=UserName)
        entry_1.place(x=240, y=280)

        label_2 = tk.Label(self, text="Password", width=20, font=("bold", 10))
        label_2.place(x=80, y=330)
        entry_2 = tk.Entry(self, textvar=Password, show="*")
        entry_2.place(x=240, y=330)

        tk.Button(self, text="Register", relief="groove", padx=5, pady=5, width=10, bg='white', fg='black', font=('helvetica 15 bold'),
                  command=lambda: master.switch_frame(PageOne)).place(x=100, y=400)

        tk.Button(self, text="Login", relief="groove", padx=5, pady=5, width=10, bg='white', fg='black', font=('helvetica 15 bold'),
                  command=dbcheck).place(x=300, y=400)
        # tk.Button(self, text="Login",relief="groove", padx=5,pady=5,width=10,bg='white',fg='black',font=('helvetica 15 bold'),
        # command=lambda: master.switch_frame(PageTwo)).place(x=300,y=400)


class PageOne(tk.Frame):


    def __init__(self, master):

        def database():
            global uname
            global password

            name1 = Fullname.get()
            email = Email.get()
            password = Password.get()
            uname = UserName.get()
            contact = Phone.get()
            # country=c.get()
            # prog=var1.get()
            conn = sqlite3.connect('data.db')
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, Fullname TEXT,Email TEXT NOT NULL UNIQUE, UserName TEXT NOT NULL UNIQUE, Password TEXT NOT NULL, Contact TEXT NOT NULL)')
            cursor.execute('INSERT INTO Users (FullName,Email,UserName,Password,Contact) VALUES(?,?,?,?,?)',
                           (name1, email, uname, password, contact))
            conn.commit()
            tkinter.messagebox.showinfo(title="Sign Up Message", message="Sign Up successful.Please Login!")

        tk.Frame.__init__(self, master)

        filename = tk.PhotoImage(file="background.jpeg")

        var = tk.IntVar()
        c = tk.StringVar()
        var1 = tk.IntVar()
        Fullname = tk.StringVar()
        Email = tk.StringVar()
        UserName = tk.StringVar()
        Phone = tk.IntVar()
        Password = tk.StringVar()

        tk.Frame.configure(self, bg='gray')
        # tk.Label(self, text="User Registration", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        label_0 = tk.Label(self, text="Sign Up Form",
                           width=20, font=("bold", 20))
        label_0.place(x=90, y=53)
        label_1 = tk.Label(self, text="FullName", width=20, font=("bold", 10))
        label_1.place(x=70, y=130)
        entry_1 = tk.Entry(self, textvar=Fullname)
        entry_1.place(x=240, y=130)
        label_2 = tk.Label(self, text="UserName", width=20, font=("bold", 10))
        label_2.place(x=70, y=180)
        entry_2 = tk.Entry(self, textvar=UserName)
        entry_2.place(x=240, y=180)
        label_3 = tk.Label(self, text="Email", width=20, font=("bold", 10))
        label_3.place(x=70, y=230)
        entry_3 = tk.Entry(self, textvar=Email)
        entry_3.place(x=240, y=230)
        label_4 = tk.Label(self, text="Phone", width=20, font=("bold", 10))
        label_4.place(x=70, y=280)
        entry_4 = tk.Entry(self, textvar=Phone)
        entry_4.place(x=240, y=280)
        label_5 = tk.Label(self, text="Password", width=20, font=("bold", 10))
        label_5.place(x=70, y=330)
        entry_5 = tk.Entry(self, textvar=Password, show="*")
        entry_5.place(x=240, y=330)

        tk.Button(self, text='Submit', width=20, bg='purple',
                  fg='red', command=database).place(x=180, y=380)
        tk.Button(self, text="Go back to start page", bg='purple', fg='red', width='20',
                  command=lambda: master.switch_frame(StartPage)).place(x=180, y=430)


class PageTwo(tk.Frame):
    def __init__(self, master):

        def cam():
            print("Starting camera")
            print("UID:" + uid)
            os.system('python3 drowsiness_yawn.py -uid '+uid+' -w 0')

        def sound_alarm():
            # play an alarm sound
            mixer.init()
            alert = mixer.Sound('alarm.wav')
            alert.play()
            time.sleep(0.1)
            alert.play()

        # def graph_data():
        #     conn = sqlite3.connect('data.db')
        #     with conn:
        #         cursor = conn.cursor()
        #     cursor.execute('SELECT Ear,DateTime FROM Analysis_Data WHERE AlertType=? AND UserId=?',('Drowsiness Alert',uid))
        #     ear = []
        #     dates = []
        #     for row in cursor.fetchall():
        #         #print(row)
        #         ear.append(row[0])
        #         dates.append(row[1])
        #
        #     plt.title('EAR calculation')
        #     plt.ylabel('EAR')
        #     plt.xlabel('Time')
        #     plt.plot_date(dates,ear,'-')
        #     plt.show()



        def browseimage_click():

            global filename
            filename = askopenfilename()
            img = Image.open(filename)
            img = img.resize((400, 400), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            # self.lbl.configure(image=img, width=400, height=400)
            # self.lbl.img = img
            capture = cv2.VideoCapture(filename)
            face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
            eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
            blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')

            while True:
                ret, frame = capture.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray)

                for (x, y, w, h) in faces:
                    font = cv2.FONT_HERSHEY_COMPLEX
                    cv2.putText(frame, 'Face', (x + w, y + h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    roi_color = frame[y:y + h, x:x + w]

                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                    blink = blink_cascade.detectMultiScale(roi_gray)
                    for (eyx, eyy, eyw, eyh) in blink:
                        cv2.rectangle(roi_color, (eyx, eyy), (eyx + eyw, eyy + eyh), (255, 255, 0), 2)
                        cv2.putText(frame, "DROWSINESS ALERT!", (20, 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.6, (255, 255, 255), 2)

                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            capture.release()
            cv2.destroyAllWindows()

        def browse_videoclick():

            global filename
            filename = askopenfilename()
            capture = cv2.VideoCapture(filename)

            face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
            eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
            blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')

            while True:
                ret, frame = capture.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray)

                for (x, y, w, h) in faces:
                    font = cv2.FONT_HERSHEY_COMPLEX
                    cv2.putText(frame, 'Face', (x + w, y + h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    roi_color = frame[y:y + h, x:x + w]

                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                    blink = blink_cascade.detectMultiScale(roi_gray)
                    for (eyx, eyy, eyw, eyh) in blink:
                        cv2.rectangle(roi_color, (eyx, eyy), (eyx + eyw, eyy + eyh), (255, 255, 0), 2)
                        cv2.putText(frame, "DROWSINESS ALERT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                    (255, 255, 255), 2)

                        sound_alarm()

                cv2.imshow('frame', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            capture.release()
            cv2.destroyAllWindows()

        # def Open_bar():
        #     GUI_BAR.bar_chart()

        def report():

            print("Generating report")
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute('SELECT DateTime FROM Analysis_Data WHERE AlertType=? AND UserId=?',
                      ('Drowsiness Alert',uid))
            res = c.fetchall()
            c.execute(
                'SELECT DateTime FROM Analysis_Data WHERE AlertType=? AND UserId=?', ('Yawn Alert', uid))

            # tkinter.messagebox.showinfo("Analysis Report", "REPORT\nUser ID:" + uid + "\nDate:" +str(date.today())+"\n Drowsiness Start Time:" +str(*res[0])+"\n Drowsiness End Time:" +str(*res[-1]))

            tkinter.messagebox.showinfo("Analysis Report", "REPORT\nUser ID:" + uid + "\nDate:" + str(date.today()) + "\n Drowsiness Times:" +str(res))




        tk.Frame.__init__(self, master)

        # def showdetails(id):
        #     try:
        #         val = int(id)
        #     except:

        #this is actually the date we are entering
        # Date = tk.StringVar()
        # dateCheck = False
        # tk.Frame.configure(self, background="gray")
        #
        # # tk.Label(self, text="WELCOME", font=(
        # #     'Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        #detection label
        Detection = customtkinter.CTkLabel(self,text="Detection",fg_color="black")
        Detection.place(x=130,y=60)

        # realtime button
        realtimeBtn = customtkinter.CTkButton(self, text="Real-time Detection", command=cam)
        realtimeBtn.place(x=130, y=90)

        # browse video button
        Browse_vid = customtkinter.CTkButton(self, text="Browse Video & Detect", command=browse_videoclick)
        Browse_vid.place(x=130, y=130)

        # browse image button
        Browse_image = customtkinter.CTkButton(self, text="Browse Image & Detect", command=browseimage_click)
        Browse_image.place(x=130, y=170)


        #analysis label
        Analysis = customtkinter.CTkLabel(self, text="Analysis",fg_color="black")
        Analysis.place(x=130,y=240)


        #date entry
        # label_5 = tk.Label(self, text="Enter Date(YYYY-MM-DD)",
        #                    width=30, font=("bold", 10))
        # label_5.place(x=130, y=270)
        #
        # entry_5 = tk.Entry(self, textvar=Date)
        #
        # entry_5.place(x=130, y=290)

        # view report button
        # customtkinter.CTkButton(self, text="Bar chart", command=Open_bar).place(x=130, y=245)

        # view report button
        customtkinter.CTkButton(self, text="View Drowsiness Analysis", command=report).place(x=130, y=280)
        # view report button
        # customtkinter.CTkButton(self, text="View Chart", command=graph_data).place(x=130, y=320)
        # go back button
        customtkinter.CTkButton(self, text="Go back to start page",
                                command=lambda: master.switch_frame(StartPage)).place(x=130, y=320)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


