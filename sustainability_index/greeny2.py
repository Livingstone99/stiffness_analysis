from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import sys
from pprint import pprint
from PIL import ImageTk, Image
import datetime as dt
import requests
import sqlite3

with sqlite3.connect('weather.db') as db:
    cursur = db.cursor()

cursur.execute("CREATE TABLE IF NOT EXISTS new(Date TEXT, City TEXT, Weather TEXT,"
               " WeatherDescription TEXT, Temperature REAL, Humidity INTEGER,"
               " WindSpeed REAL, Longitude REAL, Latitude REAL)")
db.commit()
db.close()


class moreTab(tk.Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("500x800")
        self.resizable(False, False)
        self.title('GREENY INC')
        container = Frame(self, bg='#c9e3c1')
        container.pack(side="top", fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for q in (pageone, widget):
            frame = q(container, self)
            self.frames[q] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.raise_frame(pageone)

    def raise_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class widget(Frame):
    def __init__(self, master=0, control=0):
        Frame.__init__(self, master, background='#2a5699')


class pageone(Frame):
    def __init__(self, master=0, control=0):
        Frame.__init__(self, master, background='white')
        self.bind("<Button-1>", self.unraise_menu)

        ##Database counting the
        ## the number of rows
        with sqlite3.connect('weather.db') as db:
            cursur = db.cursor()
        cursur.execute("select count(*) from new")
        self.lla = cursur.fetchone()
        self.index = self.lla[0]
        self.dxx = self.lla[0]
        s = ttk.Style()
        s.theme_use('clam')  # activebackground="#c0c0c0", bg="#c0c0c0",
        ##MENU-LIKE FRAME
        self.frame = ttk.Frame(self, width=200, relief=FLAT, height=550, style='home.TFrame')
        s.configure('home.TFrame', highlightbackground="#ffffa6",
                    highlightthickines=10, border=0, background="white")
        ## CONTENTS IN THE SECOND FRAME
        self.frame_icon1 = ImageTk.PhotoImage(file='images/wind-energy.png')
        self.frame_icon2 = ImageTk.PhotoImage(file='images/sun-energy.png')
        self.frame_icon3 = ImageTk.PhotoImage(file='images/hydro-power.png')
        self.frame_icon4 = ImageTk.PhotoImage(file='images/gas-mask.png')
        self.frame_icon5 = ImageTk.PhotoImage(file='images/mould.png')
        self.frame_icon6 = ImageTk.PhotoImage(file='images/placeholder.png')
        self.frame_icon7 = ImageTk.PhotoImage(file='images/sunset.png')
        self.frame_icon8 = ImageTk.PhotoImage(file='images/sprout.png')
        self.but_frame_icon1 = Button(self.frame, image=self.frame_icon1, activebackground="#c0c0c0", bg="#c0c0c0",
                                      border=0)
        # fg = '#808080',text = 'WIND\nENERGY',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon2 = Button(self.frame, image=self.frame_icon2, activebackground="#c0c0c0", bg="#c0c0c0",
                                      border=0)
        # fg = '#808080', text = 'SOLAR\nENERGY',font = ('times', '6', 'underline'), compound = TOP
        self.but_frame_icon3 = Button(self.frame, image=self.frame_icon3, activebackground="#c0c0c0", bg="#c0c0c0",
                                      border=0)
        # ,fg = '#808080',text = 'WATER\nENERGY',font=('times', '6', 'underline'), compound =TOP
        self.but_frame_icon4 = Button(self.frame, image=self.frame_icon4, activebackground="#c0c0c0", bg="#c0c0c0",
                                      border=0)
        # fg = '#808080',text = 'FLOOD',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon5 = Button(self.frame, image=self.frame_icon5, activebackground="#c0c0c0", bg="#c0c0c0",
                                      border=0)
        # fg = '#808080',text = 'HUMIDITY',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon6 = Button(self.frame, image=self.frame_icon6, activebackground="#c0c0c0", bg="#c0c0c0",
                                      border=0)
        # fg = '#808080',text = 'LOCATION',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon7 = Button(self.frame, image=self.frame_icon7, activebackground="#c0c0c0", bg="#c0c0c0",
                                      border=0)
        # fg = '#808080',text = 'DESERT',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon8 = Button(self.frame, image=self.frame_icon8, activebackground="#c0c0c0", bg="#c0c0c0",
                                      border=0)
        # fg = '#808080',text = 'FARMING',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon1.place(relx=0.1, rely=0.10)
        self.but_frame_icon2.place(relx=0.1, rely=0.215)
        self.but_frame_icon3.place(relx=0.1, rely=0.33)
        self.but_frame_icon4.place(relx=0.1, rely=0.445)
        self.but_frame_icon5.place(relx=0.1, rely=0.56)
        self.but_frame_icon6.place(relx=0.1, rely=0.675)
        self.but_frame_icon7.place(relx=0.1, rely=0.79)
        self.but_frame_icon8.place(relx=0.1, rely=0.805)

        ## LABELS
        ## IMAGE GOTTEN FROM <div>Icons made by <a href="https://www.flaticon.com/authors/good-ware" title="Good Ware">
        # Good Ware</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is
        # licensed by <a href="http://creativecommons.org/licenses/by/3.0/"
        # title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>

        # self.background = ImageTk.PhotoImage(file ='pexels-photo-531636.jpeg')

        self.snow_image = ImageTk.PhotoImage(file='images/snow.png')
        self.rainyy_image = ImageTk.PhotoImage(file='images/rain.png')
        self.sunny_image = ImageTk.PhotoImage(file='images/contrast.png')
        self.cloudy_sunny_image = ImageTk.PhotoImage(file='images/cloudy.png')
        self.backImgBut = ImageTk.PhotoImage(file='images/back-hand-drawn-arrow (1).png')
        self.forwardImgBut = ImageTk.PhotoImage(file='images/back-hand-drawn-arrow (3).png')
        # self.background_lab = Label(self, image=self.background)
        # self.background_lab.place(relx=0, rely=0.12)
        self.img1 = ImageTk.PhotoImage(file='images/user.png')
        s.configure('TLabel', foreground="white", background="white",
                    font=('Lucida Calligraphy', 'BOLD','15'))
        s.configure('TButton', foreground="#23a24d",border = 0, background="white",
                    font=('Franklin Gothic Demi Cond', '20'))
        s.configure('date.TLabel', foreground="#97afc6", background="#808080", font=('Georgia', '15'))
        s.configure('forecast.TLabel', foreground="#72b8b8", background="#808080", font=('Lucida Handwriting', '16'))
        s.configure('cast.TLabel', foreground="#97afc6", background="#808080",
                    font=('Lucida Handwriting', '15'))  # Constantia
        s.configure('frame.TLabel', foreground="white", background="#c0c0c0")
        self.label = ttk.Button(self, compound=BOTTOM,  text="GREENY")
        self.label.place(relx=0.05, rely=0)
        # # self.image_label = ttk.Label(self, image=self.img1)
        # # self.image_label.place(relx=0.2, rely=0.11)
        # # cont = '    ' * 50
        # self.label_frame = ttk.Label(self, text=cont, style='frame.TLabel')
        # self.label_frame.place(relx=0, rely=0)
        # self.label_bottomframe = ttk.Label(self, text=cont, style='frame.TLabel')
        # self.label_bottomframe.place(relx=0, rely=0.9)

        ##WEATHER API REQUESTING CODES
        ##CODE RESPONSIBLE FOR THE MENU WIDGET
        s.map('TFrame',
              foreground=[('disabled', "#808080"),
                          ('pressed', 'red'),
                          ('active', "#808080")],
              background=[('disabled', 'magenta'),
                          ('pressed', '!focus', "#808080"),
                          ('active', "#9a9a9a")],
              highlightcolor=[('focus', '#fdcd41'),
                              ('!focus', 'red')],
              relief=[('pressed', 'groove'),
                      ('!pressed', 'ridge')])
        self.home_but = ImageTk.PhotoImage(file='images/leaf.png')
        self.home_but_lab = Button(self, image=self.home_but, border=0,
                                   activebackground="white", bg="white", command=self.frame_raiser)
        self.home_but_lab.place(relx=0, rely=-0.0032)
        # s.configure('TMenubutton',cursor = 'circle',activebackground ="#808080",borderwidth= 0, background= "#808080")
        # self.mbb = ttk.Menubutton(self, direction='below')
        # self.mbb.menu = Menu(self.mbb, tearoff = 0)
        # self.mbb['menu'] = self.mbb.menu
        # # self.mbb.place(x = 0, y= 30)
        # self.mbb.menu.add_command(label= 'hello', command = lambda : print('hello world'))
        # self.mbb.menu.add_cascade(label= 'menu', command = lambda : print('menu is cool'))
        # # estyle = ttk.Style()
        ## THIS BUNCH OF CODES IS RESPONSIBLE FOR THE DARK BACKGROUNND OF THEENTRY BOX
        s.element_create("plain.field", "from", "clam")
        s.layout("EntryStyle.TEntry",
                 [('Entry.plain.field', {'children': [('Entry.background',
                                                       {'children': [('Entry.padding', {'children': [(
                                                           'Entry.textarea', {'sticky': 'nswe'})],
                                                           'sticky': 'nswe'})], 'sticky': 'nswe'})],
                                         'border': '2', 'sticky': 'nswe'})])
        s.configure("EntryStyle.TEntry", width=20,
                    background="white",
                    foreground="#4a6984",
                    fieldbackground="white")
        s.configure("home.TButton",
                    background="#ffffa6",
                    foreground="#4a6984",
                    activebackground='"#808080"',
                    highlightcolor='"#808080"')

        self.img2 = ImageTk.PhotoImage(file='images/search.png')
        self.flag = True
        self.search = ttk.Entry(self, style="EntryStyle.TEntry", font=('Times', '10'))
        text = 'search'
        self.search.place(x=375, y=4)
        self.search.insert(END, text)
        self.search_but = Button(self, image=self.img2, cursor='arrow',
                                 activebackground="white", bg="white",
                                 )
        self.sign_in_but = Button(self, text= 'sign-in', font=('forte', '20'), fg="#4C4C77", border = 0, width = 10,  cursor='arrow',
                                 activebackground="#ffffa6", bg="white",
                                 )
        self.sign_in_but.place(relx = 0.15, rely = 0.3)
        self.sign_up_but = Button(self, text= 'sign-up', font=('forte', '20'), fg="#4C4C77", border = 0, width = 10,  cursor='arrow',
                                 activebackground="#ffffa6", bg="white",
                                 )
        self.sign_up_but.place(relx = 0.45, rely = 0.3)

        self.search_but.place(x=475, y=3)
        self.search_but['border'] = '0'
        self.back = Button(self, image=self.backImgBut, text='PREVIOUS',
                           activebackground="#808080", bg="#808080"
                           , compound=TOP, font=('forte', '10'), fg="#4C4C77")
        self.back['border'] = '0'
        self.forward = Button(self, image=self.forwardImgBut, text='NEXT',
                              activebackground="#808080", bg="#808080"
                              , compound=TOP, font=('forte', '10'), fg="#4C4C77")

        self.forward['border'] = '0'

        ##TIME MODULE
        self.sun = ImageTk.PhotoImage(file='images/sunny (1).png')
        self.moon = ImageTk.PhotoImage(file='images/crescent-moon (1).png')
        self.twilight = ImageTk.PhotoImage(file='images/cloudy.png')
        self.dawn = ImageTk.PhotoImage(file='images/sunrise.png')
        self.daylabel = ttk.Label(self, image=self.sun)

        gui_time = dt.datetime.now()
        self.show_days = (gui_time.strftime('%I') + ':' + gui_time.strftime('%M') + gui_time.strftime('%p'))
        self.show_time = (gui_time.strftime('%b'), gui_time.strftime('%d'), gui_time.strftime('%A'))
        # self.time1 = ttk.Label(self, text=self.show_time, style='date.TLabel')
        # self.time1.place(relx=0.65, rely=0.05)
        # self.time2 = ttk.Label(self, text=self.show_days, style='date.TLabel')
        # self.time2.place(relx=0.65, rely=0.09)
        self.country = ttk.Label(self, style='date.TLabel')
        self.flagg = False
        self.error = ttk.Button(self, text='oops! weather \ncannot be found')
        self.counter = 1
        self.index = 1
        self.display = []
        self.display1 = []
        self.display_prev = []
        self.retrieve = []
        self.lists_snow = ['Fog', 'Snow', 'Mist', 'Haze']
        self.lists_rain = ['Rain', 'Drizzle']
        self.lists_sunny = ['Clear', 'Clouds']
        self.prev_count = 0
        self.dxx = self.lla[0]
        self.image_label = Label(self, image=self.img1, bg ='white' )
        self.image_label.place(relx=0.35, rely=0.13)
        self.flag = True
        self.flag_seach = True
        # self.area_details()
        self.time_control()

    def clock_tick(self):

        self.time1.config(text=self.show_time)
        self.time2.config(text=self.show_days)
        self.time1.after(200, self.clock_tick)
        self.time2.after(200, self.clock_tick)

    def time_control(self):
        self.gui_time = dt.datetime.now()
        self.day_or_night = self.gui_time.strftime('%I') + self.gui_time.strftime('%p')
        self.day = ['10AM', '11AM', '12PM', '01PM', '02PM', '03PM', '04PM', '05PM']
        self.morn = ['06AM', '07AM', '08AM', '09AM']
        self.night = ['07PM', '08PM', '09PM', '10PM', '11PM', '12AM', '01AM', '02AM', '03AM', '04AM', '05AM']
        print(self.day_or_night)
        for i in self.day:
            if self.day_or_night == i:
                self.daylabel['image'] = self.sun
                self.daylabel.place(relx=0.85, rely=0.1)
                # self.nightlabel.place_forget()
        if self.day_or_night == '06PM':
            print('its here')
            self.daylabel['image'] = self.twilight
            self.daylabel.place(relx=0.85, rely=0.1)

        for i in self.night:
            if self.day_or_night == i:
                self.daylabel['image'] = self.moon
                self.daylabel.place(relx=0.85, rely=0.1)

        for i in self.morn:
            if self.day_or_night == i:
                self.daylabel['image'] = self.dawn
                self.daylabel.place(relx=0.85, rely=0.1)

    def frame_raiser(self):
        if self.flag:
            self.frame.place(x=0, y=0)
            self.flag = False
        else:
            self.frame.place_forget()
            self.flag = True


    def unraise_menu(self, event):
        self.frame.place_forget()



app = moreTab()
app.mainloop()
