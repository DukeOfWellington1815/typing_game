import tkinter as tk
from tkinter import *
from random_words import *
import time
import threading
from sql_connector import *

SEND = sql_connector

class TypeSpeedGui():
    def __init__(self):
        # creates the root location of the windows and is where the menu is located
        self.root = Tk()
        self.root.geometry('1000x600')
        self.root.columnconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=0)

        # title of the project
        self.title = Label(self.root,text='Schreibgeschwindigkeits- und Akkuratstest \n')
        self.title.config(font=('arial',30))
        self.title.grid(column=0,row=0,columnspan=5)

        # explenation of the project
        self.menu_explanation = Label(self.root,text='Hallo und herzlich willkommen zu unserem Speed Typing Test. \nMit diesem einfachen Programm können Sie Ihre Tippgeschwindigkeit testen! \nWählen Sie unten die Satzlänge aus und wählen Sie einen der Schwierigkeitsgrade, um loszulegen.\n')
        self.menu_explanation.config(font=("gill sans mt", 15))
        self.menu_explanation.grid(column=0, row=1, columnspan=5)

        # entry for the length of the text
        self.length = Entry(self.root)
        self.length.config(width='69', font=('gill sans mt', 15))
        self.length.grid(column=0, row=2, columnspan=5)

        self.space = Label(self.root, text='')
        self.space.grid(row=3)

        # this opens a new window with the easy text
        self.easy = Button(self.root, text='Einfach', command=lambda: self.entry_not_null('e'))
        self.easy.config(font=('gill sans mt', 15))
        self.easy.grid(column=0, row=4, sticky=EW)

        # new window for the hard text
        self.difficult = Button(self.root, text='Anspruchsvoll', command=lambda: self.entry_not_null('h'))
        self.difficult.config(font=('gill sans mt', 15))
        self.difficult.grid(column=0, row=5, sticky=EW)

        # sets the time wpm to 0
        self.counter = 0
        # used for thread
        self.running = False
        # used to test if the sentance is done
        self.done = False
        # test dif
        self.dif = False

        self.root.mainloop()

    def entry_not_null(self, dif):
        #test that the length is not null then opens the easy/ hard win
        if re.search('^[1-9]', self.length.get()):
            if dif == 'e':
                self.easy_window()
            else:
                self.hard_window()

    def save_easy(self,where):
        # if the text is write with no mistakes and this button is pressed sends score to database (see sql connector class)
        if self.done:
            SEND.send_score_easy(str(self.wpm), str(self.counter), str(self.cpm))
            send_score = tk.Label(where,text='score has be saved')
            send_score.config(font=('gill wheresans mt', 15))
            send_score.grid(column=0, row=14)

    def recive_easy(self,where):
        # gets the highst data from database with select (see sql connector class)
        highscore = tk.Label(where, text=f'The Highscore is: {SEND.recive_score_easy()}')
        highscore.config(font=('gill sans mt', 15))
        highscore.grid(column=0, row=14)

    # save_hard is the same as easy just for the hard words
    def save_hard(self,where):
        if self.done:
            SEND.send_score_hard(str(self.wpm), str(self.counter), str(self.cpm))
            send_score = tk.Label(where, text='score has be saved')
            send_score.config(font=('gill wheresans mt', 15))
            send_score.grid(column=0, row=14)


    def recive_hard(self, where):
        highscore = tk.Label(where, text=f'The Highscore is: {SEND.recive_score_hard()}')
        highscore.config(font=('gill sans mt', 15))
        highscore.grid(column=0, row=14)

    # this is called when something writen in the inout text entry and starts the thread
    def start(self, event):
        if not self.running:
            # is the input key is not ctrl shift or alt
            if event.keycode not in [16, 17, 18]:
                self.running = True
                # starts the thread
                t = threading.Thread(target=self.time_thread)
                t.start()
        self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.callback(sv))

    def time_thread(self):
        # a thread is something that runs while the main program is running in our case this is the timer
        while self.running:
            inp_lst = self.input_entry.get().split()
            inp_len = len(inp_lst)
            print(inp_len)
            time.sleep(0.1)
            # counter is the time counting up every 0.1 sec
            self.counter += 0.1
            self.cps = len(self.input_entry.get()) / self.counter
            self.cpm = self.cps * 60
            self.wpm = inp_len / self.counter * 60
            # config changes the speed label and updates the time wpm cps
            self.speed_label.config(
                text=f'Geschwindigkeit: \n{self.counter:.2f} Time eplapsed\n{self.cpm:.2f}CPM\n {self.wpm:.2f}WPM')

    def easy_reset(self):
        # resets the speed label and stops the thread
        self.running = False
        self.counter = 0
        self.speed_label.config(text='Geschwindigkeit: \n0.00 CPS\n0.00 CPM\n 0.00 WPM')
        #test if the sentance is easy or hard and gives a new one
        if self.dif:
            self.sent = random_words.get_easy_sentance(int(self.length.get())) + '.'
        else:
            self.sent = random_words.get_hard_sentance(int(self.length.get())) + '.'
        self.text.config(text=self.sent)
        self.input_entry.delete(0, 'end')


    def hard_reset(self):
        # resets the speed label and stops the thread
        self.running = False
        self.counter = 0
        self.speed_label.config(text='Geschwindigkeit: \n0.00 CPS\n0.00 CPM\n 0.00 WPM')
        #test if the sentance is easy or hard and gives a new one
        if self.dif:
            self.sent = random_words.get_easy_sentance(int(self.length.get())) + '.'
        else:
            self.sent = random_words.get_hard_sentance(int(self.length.get())) + '.'
        self.text.config(text=self.sent)
        self.input_entry.delete(0, 'end')

    def callback(self, sv):
        self.sv = sv
        letter = self.sv.get()
        # this test if the lenght of what is written is the same as the sentance that has to be writen
        if letter == self.sent and len(letter) == len(self.sent):
            self.input_entry.config(fg='green')
            self.running = False
            self.done = True
        # test if the letters typed so far are the same as the sentances
        elif self.text_test(letter):
            self.input_entry.config(fg='black')
        #changes color red if the text is not the same
        else:
            self.input_entry.config(fg='red')

    def text_test(self, letter):
        word_len = len(letter)
        # test if the letters are the same
        for i in range(word_len):
            if letter[i] != self.sent[i]:
                return False
        return True

    def easy_window(self):  # new window definition
        # creates the root for the new window
        easy_window_root = Toplevel(self.root)
        easy_window_root.geometry('1000x600')
        easy_window_root.columnconfigure(0, weight=2)
        easy_window_root.rowconfigure(5, weight=0)

        # creats the title same as menu
        self.title = Label(easy_window_root, text='Schreibgeschwindigkeits- und Akkuratstest \n')
        self.title.config(font=('arial', 30))
        self.title.grid(column=0, row=0, columnspan=5)

        len = self.length.get()

        # create the random sent
        self.sent = random_words.get_easy_sentance(int(len)) + '.'

        # his gets the letter of the input
        self.sv = StringVar()
        self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.callback(sv))

        # displays speed wpm time etc
        self.speed_label = Label(easy_window_root, text='Geschwindigkeit: \n0.00 Time eplapsed\n0.00 CPM\n 0.00 WPM')
        self.speed_label.config(font=("gill sans mt", 15))
        self.speed_label.grid(row=1)

        self.text = Label(easy_window_root, text=self.sent)
        self.text.grid(row=2)
        self.text.config(font=("gill sans mt", 15))

        # where the user inputs his text
        self.input_entry = Entry(easy_window_root, textvariable=self.sv)
        # .bind test for a key press
        self.input_entry.bind("<KeyPress>", self.start)
        self.input_entry.config(width='69', font=('gill sans mt', 15))
        self.input_entry.grid(column=0, row=3, columnspan=5)

        self.space = Label(easy_window_root, text='')
        self.space.grid(row=4)

        # calls rest def
        self.reset = Button(easy_window_root, text='Zurücksetzen', command=self.easy_reset)
        self.reset.config(font=('gill sans mt', 15))
        self.reset.grid(row=5)

        # calls save easy
        self.showhighscore = Button(easy_window_root, text='Highscore anzeigen', command=lambda: self.recive_easy(easy_window_root))
        self.showhighscore.config(font=('gill sans mt', 15))
        self.showhighscore.grid(column=0, row=6)

        # calls recive hard
        self.savehighscore = Button(easy_window_root, text='Highscore speichern', command=lambda: self.save_easy(easy_window_root))
        self.savehighscore.config(font=('gill sans mt', 15))
        self.savehighscore.grid(column=0, row=7)

        self.dif = True

    def hard_window(self):  # new window definition is the same as easy win except it choose a hard sent (see random words)
        hard_window_root = Toplevel(self.root)
        hard_window_root.geometry('1000x600')
        hard_window_root.columnconfigure(0, weight=2)
        hard_window_root.rowconfigure(5, weight=0)

        self.title = Label(hard_window_root, text='Schreibgeschwindigkeits- und Akkuratstest \n')
        self.title.config(font=('arial', 30))
        self.title.grid(column=0, row=0, columnspan=5)

        len = self.length.get()

        self.sent = random_words.get_hard_sentance(int(len)) + '.'

        self.sv = StringVar()
        self.sv.trace("w", lambda name, index, mode, sv=self.sv: self.callback(sv))

        self.speed_label = Label(hard_window_root, text='Geschwindigkeit: \n0.00 Time eplapsed\n0.00 CPM\n 0.00 WPM')
        self.speed_label.config(font=("gill sans mt", 15))
        self.speed_label.grid(row=1)

        self.text = Label(hard_window_root, text=self.sent)
        self.text.grid(row=2)
        self.text.config(font=("gill sans mt", 15))

        self.input_entry = Entry(hard_window_root, textvariable=self.sv)
        self.input_entry.bind("<KeyPress>", self.start)
        self.input_entry.config(width='69', font=('gill sans mt', 15))
        self.input_entry.grid(column=0, row=3, columnspan=5)

        self.space = Label(hard_window_root, text='')
        self.space.grid(row=4)

        self.reset = Button(hard_window_root, text='Zurücksetzen', command=self.hard_reset)
        self.reset.config(font=('gill sans mt', 15))
        self.reset.grid(row=5)

        self.showhighscore = Button(hard_window_root, text='Highscore anzeigen', command=lambda: self.recive_hard(hard_window_root))
        self.showhighscore.config(font=('gill sans mt', 15))
        self.showhighscore.grid(column=0, row=6)

        self.savehighscore = Button(hard_window_root, text='Highscore speichern', command=lambda: self.save_hard(hard_window_root))
        self.savehighscore.config(font=('gill sans mt', 15))
        self.savehighscore.grid(column=0, row=7)

        self.dif = False


if __name__ == "__main__":
    TypeSpeedGui()
