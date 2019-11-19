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
from HoverInfo import HoverInfo

with sqlite3.connect('weather.db') as db:
    cursur = db.cursor()

cursur.execute("CREATE TABLE IF NOT EXISTS new(Date TEXT, City TEXT, Weather TEXT,"
                    " WeatherDescription TEXT, Temperature REAL, Humidity INTEGER,"
                    " WindSpeed REAL, Longitude REAL, Latitude REAL)")
db.commit()
db.close()
class moreTab(tk.Tk):
    def __init__(self):
        Tk.__init__(self )
        self.geometry("1350x800")
        self.resizable(False, False)
        self.title('CHECK SUSTAINABILITY')
        self.iconbitmap('images/Pixelkit-Flat-Jewels-Tree.ico')
        container = Frame(self, bg='white')
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
        Frame.__init__(self, master, background='#32db8f')
class pageone(Frame):
    def __init__(self, master =0, control=0):
        Frame.__init__(self,  master,background ='#00bfc0' )
        self.bind("<Button-1>", self.unraise_menu)
        ## started here hover stuff
        # self.place()
        # self.lbl = Label(self, text = 'solar')
        # self.lbl.place()
        # self.hover = HoverInfo(self, )
        ##Database counting the
        ## the number of rows
        with sqlite3.connect('weather.db') as db:
            cursur = db.cursor()
        cursur.execute("select count(*) from new")
        self.lla = cursur.fetchone()
        self.index = self.lla[0]
        self.dxx = self.lla[0]
        s = ttk.Style()
        s.theme_use('clam')#activebackground="#c0c0c0", bg="#c0c0c0",
        ##MENU-LIKE FRAME
        self.frame = ttk.Frame(self, width=48, relief=FLAT, height=550,style = 'home.TFrame')
        s.configure('home.TFrame',highlightbackground ="#808080",
                    highlightthickines =10,border = 0,background ="#c0c0c0" )
        ## CONTENTS IN THE SECOND FRAME
        self.frame_icon1 = ImageTk.PhotoImage(file='images/wind-energy.png')
        self.frame_icon2 = ImageTk.PhotoImage(file='images/sun-energy.png')
        self.frame_icon3 = ImageTk.PhotoImage(file='images/hydro-power.png')
        self.frame_icon4 = ImageTk.PhotoImage(file='images/gas-mask.png')
        self.frame_icon5 = ImageTk.PhotoImage(file='images/mould.png')
        self.frame_icon6 = ImageTk.PhotoImage(file='images/placeholder.png')
        self.frame_icon7 = ImageTk.PhotoImage(file='images/sunset.png')
        self.frame_icon8 = ImageTk.PhotoImage(file='images/sprout.png')
        self.but_frame_icon1 = Button(self.frame,cursor = 'fleur',image = self.frame_icon1,activebackground="#c0c0c0", bg="#c0c0c0",border =0)
        #fg = '#808080',text = 'WIND\nENERGY',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon2 = Button(self.frame,cursor = 'fleur',image = self.frame_icon2,activebackground="#c0c0c0", bg="#c0c0c0",border =0)
        #fg = '#808080', text = 'SOLAR\nENERGY',font = ('times', '6', 'underline'), compound = TOP
        self.but_frame_icon3 = Button(self.frame,cursor = 'fleur',image = self.frame_icon3,activebackground="#c0c0c0", bg="#c0c0c0",border =0)
        #,fg = '#808080',text = 'WATER\nENERGY',font=('times', '6', 'underline'), compound =TOP
        self.but_frame_icon4 = Button(self.frame,cursor = 'fleur',image = self.frame_icon4,activebackground="#c0c0c0", bg="#c0c0c0",border =0)
        #fg = '#808080',text = 'FLOOD',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon5 = Button(self.frame,cursor = 'fleur',image = self.frame_icon5,activebackground="#c0c0c0", bg="#c0c0c0",border =0)
        #fg = '#808080',text = 'HUMIDITY',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon6 = Button(self.frame,cursor = 'fleur',image = self.frame_icon6,activebackground="#c0c0c0", bg="#c0c0c0",border =0)
        #fg = '#808080',text = 'LOCATION',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon7 = Button(self.frame,cursor = 'fleur',image = self.frame_icon7,activebackground="#c0c0c0", bg="#c0c0c0",border =0)
        #fg = '#808080',text = 'DESERT',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon8 = Button(self.frame,cursor = 'fleur',image = self.frame_icon8,activebackground="#c0c0c0", bg="#c0c0c0",border =0)
        #fg = '#808080',text = 'FARMING',font=('times', '6', 'underline'), compound =TOP,
        self.but_frame_icon1.place(relx =0.1,rely =  0.10)
        self.but_frame_icon2.place(relx =0.1,rely =  0.215)
        self.but_frame_icon3.place(relx =0.1,rely =  0.33)
        self.but_frame_icon4.place(relx =0.1,rely =  0.445)
        self.but_frame_icon5.place(relx =0.1,rely =  0.56)
        self.but_frame_icon6.place(relx =0.1,rely =  0.675)
        self.but_frame_icon7.place(relx =0.1,rely =  0.79)
        self.but_frame_icon8.place(relx =0.1,rely =  0.805)
        # self.hover = HoverInfo(self, 'while hovering press return \n for an exciting msg',self.clock_tick)
        ## LABELS
        ## IMAGE GOTTEN FROM <div>Icons made by <a href="https://www.flaticon.com/authors/good-ware" title="Good Ware">
        # Good Ware</a> from <a href="https://www.flaticon.com/" 			    title="Flaticon">www.flaticon.com</a> is
        # licensed by <a href="http://creativecommons.org/licenses/by/3.0/"
        # title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>


        # self.background = ImageTk.PhotoImage(file ='pexels-photo-531636.jpeg')

        self.snow_image = ImageTk.PhotoImage(file ='images/snow.png')
        self.rainyy_image = ImageTk.PhotoImage(file ='images/rain.png')
        self.sunny_image = ImageTk.PhotoImage(file ='images/contrast.png')
        self.cloudy_sunny_image = ImageTk.PhotoImage(file ='images/cloudy.png')
        self.backImgBut= ImageTk.PhotoImage(file ='images/back-hand-drawn-arrow (1).png')
        self.forwardImgBut= ImageTk.PhotoImage(file ='images/back-hand-drawn-arrow (3).png')
        # self.background_lab = Label(self, image=self.background)
        # self.background_lab.place(relx=0, rely=0.12)
        ## these are for the buttons on the main page of the software
        self.img1 = ImageTk.PhotoImage(file = 'images/green-energy.png')
        self.imgg2 = ImageTk.PhotoImage(file = 'images/ecology.png')
        self.imgg3 = ImageTk.PhotoImage(file = 'images/plastic.png')
        self.imgg4 = ImageTk.PhotoImage(file = 'images/power-plant.png')
        self.imgg5= ImageTk.PhotoImage(file = 'images/garbage.png')
        self.imgg6 = ImageTk.PhotoImage(file = 'images/recycling.png')
        self.imgg7 = ImageTk.PhotoImage(file = 'images/population.png')
        self.imgg8 = ImageTk.PhotoImage(file = 'images/waste.png')
        self.imgg9 = ImageTk.PhotoImage(file = 'images/noise.png')
        self.imgg10 = ImageTk.PhotoImage(file = 'images/radiation.png')
        self.imgg11 = ImageTk.PhotoImage(file = 'images/smoke.png')
        s.configure('TLabel',foreground ="black", background ="#00bfc0",
                    font =('georgia', '15') )
        s.configure('TButton',foreground ="black", background ="#00bfc0",
                    font =('georgia', '15'),border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0" )
        s.configure('date.TLabel',foreground ="black", background ="#00bfc0", font =('Georgia', '15') )
        s.configure('forecast.TLabel',foreground ="black", background ="#00bfc0", font =('georgia', '16') )
        s.configure('cast.TLabel',foreground ="black", background ="#00bfc0", font =('georgia', '15') )#Constantia
        s.configure('frame.TLabel', foreground ="white", background ="#c0c0c0")
        self.label = ttk.Label(self,compound = BOTTOM,text = "FIND THE CONDUCIVENESS OF ANY \nLOCATION")
        self.label.place(relx = 0.1, rely = 0.04)
        self.image_label =Button(self, cursor = 'fleur',image =self.img1,foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label.place(relx =0.18, rely = 0.11)
        self.image_label1 =Button(self, image =self.imgg2,cursor = 'fleur',foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label1.place(relx =0.36, rely = 0.11)
        self.image_label2 =Button(self, image =self.imgg3,cursor = 'fleur',foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label2.place(relx =0.18, rely = 0.3)
        self.image_label3=Button(self, image =self.imgg4,cursor = 'fleur', foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label3.place(relx =0.36, rely = 0.3)
        self.image_label4=Button(self, image =self.imgg5,cursor = 'fleur', foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label4.place(relx =0.18, rely = 0.5)
        self.image_label5=Button(self, image =self.imgg6,cursor = 'fleur', foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label5.place(relx =0.36, rely = 0.5)
        self.image_label6=Button(self, image =self.imgg7, cursor = 'fleur',foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label6.place(relx =0.16, rely = 0.7)
        self.image_label7=Button(self, image =self.imgg8,cursor = 'fleur', foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label7.place(relx =0.36, rely = 0.7)
        self.image_label8 = Button(self, image =self.imgg9,cursor = 'fleur', foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label8.place(relx =0.52, rely = 0.11)
        self.image_label9 = Button(self, image =self.imgg10,cursor = 'fleur', foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label9.place(relx =0.52, rely = 0.3)
        self.image_label10 = Button(self, image =self.imgg11,cursor = 'fleur', foreground ="black", background ="#00bfc0",
                    border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        self.image_label10.place(relx =0.52, rely = 0.5)
        # self.image_label11 = Button(self, image =self.imgg12, foreground ="black", background ="#00bfc0",
        #             border = 0,highlightcolor = '#00bfc0',activebackground="#00bfc0")
        # self.image_label11.place(relx =0.52, rely = 0.7)
        ## this code is for the ash pane where the search entry box is located
        cont = '    '*100
        self.label_frame = ttk.Label(self,style = 'frame.TLabel' , text = cont)
        self.label_frame.place(relx =0, rely =0)
        self.label_bottomframe = ttk.Label(self,text = cont,style = 'frame.TLabel')
        self.label_bottomframe.place(relx =0, rely =0.9)

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
        self.home_but = ImageTk.PhotoImage(file = 'images/menu (1).png')
        self.home_but_lab= Button(self,image= self.home_but,border = 0,
                                  activebackground="#c0c0c0", bg="#c0c0c0",command= self.frame_raiser )
        self.home_but_lab.place(relx=0,rely= -0.0032)
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
        s.configure("EntryStyle.TEntry",width = 10,
                         background="#c0c0c0",
                         foreground="#4a6984",
                         fieldbackground="#c0c0c0")
        s.configure("home.TButton",
                         background="#c0c0c0",
                         foreground="#4a6984",
                         activebackground= '"#808080"',
        highlightcolor='"#808080"')

        self.img2 = ImageTk.PhotoImage(file = 'images/globe (2).png')
        self.flag = True
        self.search = ttk.Entry(self, style="EntryStyle.TEntry", font=('georgia', '10'))
        self.search.bind('<Button-1>', self.search_clear)
        text = 'search'
        self.search.place(relx = 0.85, rely=0.006)
        self.search.insert(END, text)
        self.search_but = Button(self, image=self.img2, cursor='arrow',
            activebackground="#c0c0c0", bg="#c0c0c0",
                                 command = lambda: self.push_requestss(self.search.get()))
        self.search_but.place(relx = 0.97, rely=0.0052)
        self.search_but['border'] = '0'
        self.back = Button(self, image = self.backImgBut, text = 'PREVIOUS',
                               activebackground="#00bfc0", bg="#00bfc0"
                            , compound = TOP,font =('georgia', '10'),fg = "black" ,command = self.history_previous)
        self.back['border'] = '0'
        self.forward = Button(self, image = self.forwardImgBut, text = 'NEXT',
                               activebackground="#00bfc0", bg="#00bfc0"
                            , compound = TOP,font =('georgia', '10'),fg ="black" ,command = self.history_next)

        self.forward['border'] = '0'

        ##TIME MODULE
        self.sun = ImageTk.PhotoImage(file='images/sun_day.png')
        self.moon = ImageTk.PhotoImage(file='images/crescent-moon (1).png')
        self.twilight = ImageTk.PhotoImage(file='images/cloudy.png')
        self.dawn = ImageTk.PhotoImage(file='images/sunseting.png')
        self.daylabel = ttk.Label(self, image=self.sun)

        gui_time = dt.datetime.now()
        self.show_days = (gui_time.strftime('%I')+':'+gui_time.strftime('%M')+gui_time.strftime('%p'))
        self.show_time = (gui_time.strftime('%b'),gui_time.strftime('%d'),gui_time.strftime('%A'))
        self.time1 = ttk.Label(self, text =self.show_time,style ='date.TLabel')
        self.time1.place(relx = 0.65, rely = 0.05)
        self.time2= ttk.Label(self, text =self.show_days,style='date.TLabel')
        self.time2.place(relx = 0.65, rely = 0.09)
        self.country =ttk.Label(self,style = 'date.TLabel')
        self.flagg =False
        self.error = ttk.Label(self, text='oops! weather \ncannot be found')
        self.counter = 1
        self.index = 1
        self.display = []
        self.display1 = []
        self.display_prev = []
        self.retrieve = []
        self.lists_snow = ['Fog', 'Snow','Mist','Haze']
        self.lists_rain = ['Rain','Drizzle']
        self.lists_sunny= ['Clear','Clouds']
        self.prev_count =0
        self.dxx = self.lla[0]
        self.back.place(relx=0, rely=0.77)
        self.flag = True
        self.flag_seach = True
        # self.area_details()
        self.time_control()
        ## to displays the button function whenever the cursor scrolls over
        ## the button
        if self.but_frame_icon1['activebackground']=='active':
            Label(self.frame, text = 'solar', bg = 'red').place(relx = .2, rely = .2)

    def clock_tick(self):
## this function is aimed at making the clock tick while the mainloop is running
        self.time1.config(text = self.show_time)
        self.time2.config(text = self.show_days)
        self.time1.after(200, self.clock_tick)
        self.time2.after(200, self.clock_tick)

    def time_control(self):
        ## this is reponsible for time and date accuracy
        self.gui_time = dt.datetime.now()
        self.day_or_night = self.gui_time.strftime('%I')+ self.gui_time.strftime('%p')
        self.day = ['10AM','11AM','12PM','01PM','02PM','03PM','04PM','05PM']
        self.morn =['06AM','07AM','08AM','09AM']
        self.night = ['07PM','08PM','09PM','10PM','11PM','12AM','01AM','02AM','03AM','04AM','05AM']
        print(self.day_or_night)
        for i in self.day:
            if self.day_or_night == i:
                self.daylabel['image'] = self.sun
                self.daylabel.place(relx=0.85, rely=0.1)
                Label(self, text = 'Good Afternoon', font =('georgia','13'), fg = '#ff3900',bg = '#00bfc0' ).place(relx=0.86, rely=0.3)

                #self.nightlabel.place_forget()
        if self.day_or_night == '06PM':
            print('its here')
            self.daylabel['image'] = self.twilight
            self.daylabel.place(relx=0.85, rely=0.1)
            Label(self, text='Good Evening',font =('georgia','13'), fg = '#838383',bg = '#00bfc0').place(relx=0.86, rely=0.3)

        for i in self.night:
            if self.day_or_night == i:
                self.daylabel['image'] = self.moon
                self.daylabel.place(relx =0.85, rely = 0.1 )
                Label(self, text = 'Good Nite',font =('georgia','13'), fg = 'black',bg = '#00bfc0').place(relx=0.86, rely=0.3)

        for i in self.morn:
            if self.day_or_night == i:
                self.daylabel['image'] = self.dawn
                self.daylabel.place(relx=0.85, rely=0.1)
                Label(self, text = 'Good morning',font =('georgia','13'), fg = '#ffd18c',bg = '#00bfc0').place(relx=0.86, rely=0.3)

    def frame_raiser(self):
        ## this responsible for the menu pop up and close
        if self.flag:
            self.frame.place(x=0, y=0)
            self.flag = False
        else:
            self.frame.place_forget()
            self.flag = True
    def search_clear(self,event):
        ## this is responsible click-clear mechnism in search entry box
        if self.flag_seach == True:
            self.search.delete(0, tk.END)
            self.flag_seach = False
    def unraise_menu(self,event):
            self.frame.place_forget()

    def area_details(self,city = 0):
        ## the aim of this function of is to relate you
        ## location to where you search (proximity check)
        # urll = 'https://raw.githubusercontent.com/meMo-Minsk/all-countries-and-cities-json/master/countries.json'
        url = 'http://restcountries.eu/rest/v2/region/africa'
        url1 = 'http://restcountries.eu/rest/v2/region/europe'
        url2 = 'http://restcountries.eu/rest/v2/region/Americas'
        url3 = 'http://restcountries.eu/rest/v2/region/Oceanic'
        url4 = 'http://restcountries.eu/rest/v2/region/asia'
        dict = {}
        mm =[]
        datas =[]
        country = []
        list = [url, url1, url2,url3,url4]
        list3 = ['Africa', 'Europe', 'Americas', 'Oceanic','Asia']
        df = -1
        for i in list:
            df +=1
            for m in list3:
                dict[i] =list3[df]

        print(dict)

        # for i in list:
        #     for k in list1:
        #         k = requests.get(i)
        #         mm = k.json()
        xd = -1
        for i in dict.keys():
            xd +=1
            mm.append(requests.get(i))
            datas.append(mm[xd].json())
        # print(mm)
        # print(datas,'\ntotal',len(datas))
        for i in datas:
            for s in range(len(i)):
                country.append(i[s]['name'])
        print(country, '\ntotal',len(country))
    #     # for i in mm
    def air_pollution(self, city=0):
        link_api = 'http://api.openweathermap.org/pollution/v1/co/{{lat},{lon}}/{datetime}.json?appid=61456b4e3589e98e00d2427a96e45497'
    def push_requestss(self, city):
        ## this function pulls data from wheather api and
        ## show the weather condition of that location
        self.prev_count += 1
        yy = 0.15
        self.clear_everything()
        try:

            self.url = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID" \
                  "=61456b4e3589e98e00d2427a96e45497&units=metric".format(city)
            self.country['text'] = city.title()
            #self.area_details(city)
            resquestt = requests.get(self.url)
            self.data = resquestt.json()
            weather = str(self.data['weather'][0]['main'])
            weather_des = str(self.data['weather'][0]['description'])
            temperature = str(self.data['main']['temp']) + "'C"
            humidityy =str(self.data['main']['humidity']) + 'g/m3'
            wind_speed =str(self.data['wind']['speed']) + 'm/s'
            longitude_latitude = str(self.data['coord']['lon']) + ' long'+\
                                 '\n\n'+str(self.data['coord']['lat']) + ' lat'
            weather1 = 'WEATHER..'
            weather_des1 = "weather description..."
            temperature1 = 'Temperature...'
            humidityy1 = 'Humidity...'
            wind_speed1 ='Windspeed... '
            longitude_latitude1 = 'Longitude...\n\nLatitude...'
            parameter = [weather, weather_des, temperature, humidityy, wind_speed, longitude_latitude]
            parameter1 = [weather1, weather_des1, temperature1, humidityy1, wind_speed1, longitude_latitude1]
            self.country.place(relx=0.5, rely=0.16)
            for i in parameter1:
                self.display1.append(ttk.Label(self,style ='cast.TLabel', text = i))
            for i in self.display1:
                yy += 0.0873
                i.place(relx=0.15, rely=yy)
            yy = 0.15
            for i in parameter:
                self.display.append(ttk.Label(self,style ='forecast.TLabel', text = i))
            print('parameter',parameter)
            for i in self.display:
                yy += 0.085
                i.place(relx = 0.65, rely = yy)
            ## loop these images into?
            ## a loop that runs only during the Day(7am-6pm)
            self.image_label['image'] = self.sunny_image
            for i in self.lists_snow:
                if str(self.data['weather'][0]['main']) ==i:
                    self.image_label['image'] = self.snow_image
            for i in self.lists_rain:
                if str(self.data['weather'][0]['main']) == i:
                    self.image_label['image'] = self.rainyy_image
            if str(self.data['weather'][0]['main']) == 'Clear':
                self.image_label['image'] = self.sunny_image
            if str(self.data['weather'][0]['main']) == 'Clouds':
                self.image_label['image'] = self.cloudy_sunny_image
            self.database(city)
        except KeyError:
            for i in self.display:
                i.place_forget()
            self.error.place(relx =0.3, rely = 0.4)
    def database(self,city):
        ## this is responsible for the recall of the
        ## of the various searches that hasbeing made
        with sqlite3.connect('weather.db') as db:
            cursur = db.cursor()
        datab = dt.datetime.now()
        date = datab.strftime('%d-%m-%Y  %H:%M%A')

        self.counter +=1
        weather =  str(self.data['weather'][0]['main'])
        weatherDes = str(self.data['weather'][0]['description'])
        temper = str(self.data['main']['temp'])
        humid =str( self.data['main']['humidity'])
        windsp = str(self.data['wind']['speed'])
        longi= str(self.data['coord']['lon'])
        latit = str(self.data['coord']['lat'])

        cursur.execute("INSERT INTO new(Date, City, Weather, WeatherDescription, "
                    "Temperature, Humidity, WindSpeed, Longitude, Latitude) VALUES(?,?,?,?,?,?,?,?,?)",
                    (date, city, weather, weatherDes,temper,humid,windsp, longi,latit))


        db.commit()
        cursur.close()

        # self.counter =self.counter+self.index
    def history_previous(self):

        self.clear_some()
        self.counter -=1
        self.forward.place(relx=0.85, rely=0.77)
        with sqlite3.connect('weather.db') as db:
            cursur = db.cursor()
        cursur.execute("SELECT *FROM new ORDER BY rowid DESC LIMIT 1")
        retrieved =cursur.fetchone()
        self.index -=1
        if self.index >1:
            cursur.execute("SELECT *FROM new WHERE rowid = ?", [(self.index)])
            retrieved = cursur.fetchone()
        elif self.index==0:
            self.index = self.dxx
        yy = -0.02
        for i in retrieved:
            self.retrieve.append(ttk.Label(self, style='forecast.TLabel', text=i))
        for i in self.retrieve:
            yy += 0.085
            i.place(relx=0.65, rely=yy)
        self.retrieve[0].place_forget()
        self.retrieve[1].place_forget()
        self.retrieve[0].place(relx=0.15, rely=0.8)
        self.retrieve[1].place(relx=0.5, rely=0.16)

        # loop these images into
        # a loop that runs only during the Day(7am-6pm)
        # self.image_label['image'] = self.sunny_image
        # self.image_label.place_forget()
        print(str(retrieved[2]))
        for i in self.lists_snow:
            if str(retrieved[2]) == i:
                self.image_label['image'] = self.snow_image
        for i in self.lists_rain:
            if str(retrieved[2]) == i:
                self.image_label['image'] = self.rainyy_image
        if str(retrieved[2]) == 'Clear':
            self.image_label['image'] = self.sunny_image
        if str(retrieved[2]) == 'Clouds':
            self.image_label['image'] = self.cloudy_sunny_image
        weather1 = 'WEATHER..'
        weather_des1 = "weather description..."
        temperature1 = 'Temperature...'
        humidityy1 = 'Humidity...'
        wind_speed1 = 'Windspeed... '
        longitude_latitude1 = 'Longitude...\n\nLatitude...'
        parameter11 = [weather1, weather_des1, temperature1, humidityy1, wind_speed1, longitude_latitude1]
        for i in parameter11:
            self.display_prev.append(ttk.Label(self, style='cast.TLabel', text=i))
        yx = 0.15
        for i in self.display_prev:
            yx += 0.0873
            i.place(relx=0.15, rely=yx)
        self.display_prev.clear()
        # yyx = 0.15
        if self.index == 0:
            cursur.execute("SELECT *FROM new ORDER BY rowid DESC LIMIT 1")
            retrievedd = cursur.fetchone()
            print(retrievedd)
        # for i in parameter:
        #     self.display.append(ttk.Label(self, style='forecast.TLabel', text=i))
        # print('parameter', parameter)
        # for i in self.display:
        #     yy += 0.085
        #     i.place(relx=0.65, rely=yy)
    def history_next(self):
        self.dxx = self.lla
        self.clear_some()
        with sqlite3.connect('weather.db') as db:
            cursur = db.cursor()
        cursur.execute("SELECT *FROM new ORDER BY rowid DESC LIMIT 1")
        retrieved =cursur.fetchone()
        self.index +=1
        try:
            cursur.execute("SELECT *FROM new WHERE rowid = ?", [(self.index)])
            self.retrieved = cursur.fetchone()
        except TypeError:
            self.index = self.dxx
            cursur.execute("SELECT *FROM new WHERE rowid = ?", [(self.index)])
            self.retrieved = cursur.fetchone()
        yy = -0.02
        try:
            for i in self.retrieved:
                self.retrieve.append(ttk.Label(self, style='forecast.TLabel', text=i))
            for i in self.retrieve:
                yy += 0.085
                i.place(relx=0.65, rely=yy)
            self.retrieve[0].place_forget()
            self.retrieve[1].place_forget()
            self.retrieve[0].place(relx=0.15, rely=0.8)
            self.retrieve[1].place(relx=0.5, rely=0.16)

            # loop these images into
            # a loop that runs only during the Day(7am-6pm)
            # self.image_label['image'] = self.sunny_image
            # self.image_label.place_forget()
            # print(str(self.retrieved[2]))
            for i in self.lists_snow:
                if str(self.retrieved[2]) == i:
                    self.image_label['image'] = self.snow_image
            for i in self.lists_rain:
                if str(self.retrieved[2]) == i:
                    self.image_label['image'] = self.rainyy_image
            if str(self.retrieved[2]) == 'Clear':
                self.image_label['image'] = self.sunny_image
            if str(self.retrieved[2]) == 'Clouds':
                self.image_label['image'] = self.cloudy_sunny_image
        except TypeError:
            pass
        # yyx = 0.15
        if retrieved is None:
            cursur.execute("SELECT *FROM new ORDER BY rowid DESC LIMIT 1")
            retrievedd = cursur.fetchone()
            print(retrievedd)
        # for i in parameter:
        #     self.display.append(ttk.Label(self, style='forecast.TLabel', text=i))
        # print('parameter', parameter)
        # for i in self.display:
        #     yy += 0.085
        #     i.place(relx=0.65, rely=yy)
    def clear_everything(self):
        for i in self.display:
            i.place_forget()
        for i in self.display1:
            i.place_forget()
        self.error.place_forget()
        self.country.place_forget()
        self.display.clear()
        self.display1.clear()
        self.clear_some()
    def clear_some(self):
        for i in self.display:
            i.place_forget()
        for i in self.retrieve:
            i.place_forget()
        self.error.place_forget()
        self.country.place_forget()
        self.display.clear()
        self.retrieve.clear()
    def Windmill(self):
        pass
    def solar_intensity(self):
        pass
    def population_analysis(self):
        pass
    def waste_management(self):
        pass

app = moreTab()
app.mainloop()
