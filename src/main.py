""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Assignment: 2 - White Star Line
Author: Javid Yousaf
Student id: 201385963
Date: 15/05/2020

Description: Main script to execute the analysis on the icebergs
"""

import matplotlib
matplotlib.use('TkAgg')
from tkinter import Tk, Label, Button, filedialog
import os
import csv
import random
import operator
import matplotlib.pyplot

# Define a main application class to set up the GUI layout and interaction
class MainApplication:
    def __init__(self, master):
        self.master = master
        master.title("White Star Line Analysis")
        master.wm_iconbitmap('assets/iceberg.ico')
        master.geometry("500x400")

        self.lidar = []
        self.radar = []
        self.is_radar_loaded = False
        self.is_lidar_loaded = False
        self.canvas = []

        fig = matplotlib.pyplot.figure(figsize=(2, 2))

        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=master)
        self.canvas._tkcanvas.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        exit_button = Button(master, text='Exit', command=master.quit)
        lidar_button = Button(master, text="Open Lidar file", command=self.open_lidar)
        radar_button = Button(master, text="Open Radar file", command=self.open_radar)

        lidar_button.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5)
        radar_button.grid(row=1, column=0, ipadx=5, ipady=5, padx=5, pady=5)
        exit_button.grid(row=3, column=0, ipadx=5, ipady=5, padx=5, pady=5)

    # Open a lidar file dialog box and process file
    def open_lidar(self):
        lidar_filename = filedialog.askopenfilename(
            initialdir="/", title="Open Lidar File", filetypes=[("lidar files", ".lidar"), ("all files", ".*")])  # maybe just restrict to .lidar only
        lidar_label = Label(
            self.master, text=os.path.basename(lidar_filename))
        lidar_label.grid(row=0, column=1)
        if not lidar_filename:
            return
        try:
            with open(lidar_filename, 'r') as f:
                reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
                for row in reader:
                    rowlist = []
                    for value in row:
                        rowlist.append(value)
                    self.lidar.append(rowlist)
                self.is_lidar_loaded = True
                self.plot_data()
        except Exception as e:
            print('Unable to open file: %r' % lidar_filename, e)

    def open_radar(self):
        radar_filename = filedialog.askopenfilename(
            initialdir="/", title="Open Radar File", filetypes=[("radar files", "*.radar"), ("all files", ".*")])  # maybe just restrict to .radar only
        radar_label = Label(
            self.master, text=os.path.basename(radar_filename))
        radar_label.grid(row=1, column=1)
        if not radar_filename:
            return
        try:
            with open(radar_filename, 'r') as f:
                reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
                for row in reader:
                    rowlist = []
                    for value in row:
                        rowlist.append(value)
                    self.radar.append(rowlist)
                self.is_radar_loaded = True
                self.plot_data()
        except Exception as e:
            print('Unable to open file: %r' % radar_filename, e)

    def plot_data(self):

        if (self.is_radar_loaded & self.is_lidar_loaded):
            matplotlib.pyplot.xlim(0, 299)
            matplotlib.pyplot.ylim(0, 299)
            matplotlib.pyplot.imshow(self.radar)
            matplotlib.pyplot.imshow(self.lidar)
            self.canvas.draw()


root = Tk()
my_app = MainApplication(root)
root.mainloop()
