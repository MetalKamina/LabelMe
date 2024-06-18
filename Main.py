import json
import sys
from tkinter import *
from numpy import genfromtxt

data = json.load(open(sys.argv[1]))
ml_data = genfromtxt('data.csv',delimiter=',',dtype=None)

class data_manager:
    def __init__(self,config):
        # run checks
        try:
            if(config["data_type"] not in ["text"]):
                print("Unknown data type")
                exit()
        except KeyError:
            print("Key error. See documentation for examples.")

        # init tkinter window
        self.root = Tk()
        self.root.title("Labeler")
        self.root.geometry('350x200')

        # init the data label
        self.cfg = config
        self.n_data = 0
        self.lbl = Label(self.root,text=ml_data[self.n_data])
        self.lbl.pack()

        # init the label buttons
        for i in range(len(self.cfg['labels'])):
            b = Button(self.root,text=self.cfg['labels'][i],fg='black',command=lambda id=self.cfg['labels'][i]: self.btn_action(id))
            b.pack()

    def btn_action(self,id):
        # generate string to write to file
        to_write = f"\"{ml_data[self.n_data].decode('utf-8')}\"," #if dtype is image then write file location
        if(self.cfg['data_type'] == "image"):
            to_write = ""

        # write string to file
        open(self.cfg['outfile'],'a+').write(f"{to_write}{id}\n")

        # change label to next one
        if(self.n_data < ml_data.shape[0]-1):
            self.n_data+=1
            self.lbl.configure(text=ml_data[self.n_data])
        else:
            exit()

    # wrapper on mainloop, but might do more in the future?
    def start(self):
        self.root.mainloop()

d = data_manager(data)
d.start()