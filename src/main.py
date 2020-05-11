""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Assignment: 2 - White Star Line
Author: Javid Yousaf
Student id: 201385963
Date: 15/05/2020

Description: Main script to execute the analysis on the icebergs
"""
import areaElementAgent
from tkinter import Tk, Label, Button, filedialog, Menu, LabelFrame
import os
import csv
import random
import operator
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


# Define a main application class to set up the GUI layout and interaction
class MainApplication:
    def __init__(self, master):
        self.master = master
        master.title("White Star Line Analysis")
        master.wm_iconbitmap('assets/iceberg.ico')
        master.geometry("820x800+10+10")

        self.lidar_data = []
        self.radar_data = []

        self.berg_data = []

        self.is_radar_loaded = False
        self.is_lidar_loaded = False

        self.canvas = []

        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Default Processing",
                             command=self.process_default)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)

        # Overide the default X button to quit the application gracefully
        master.protocol("WM_DELETE_WINDOW", master.quit)

        fig_analysis = plt.figure(figsize=(8, 6))

        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(
            fig_analysis, master=master)

        self.canvas._tkcanvas.grid(
            row=3, column=0, columnspan=8, padx=10, pady=5)

        exit_button = Button(master, text='Exit', command=master.quit)

        self.process_frame = LabelFrame(master, text="Default Processing")
        self.load_frame = LabelFrame(master, text="Manual File Load")

        self.process_frame.grid(row=0, column=0, ipadx=5,
                                ipady=5, padx=5, pady=5, sticky="W")
        self.load_frame.grid(row=0, column=1, ipadx=5,
                             ipady=5, padx=5, pady=5, sticky="W")

        process_button = Button(
            self.process_frame, text="Run Process", command=self.process_default)
        lidar_button = Button(
            self.load_frame, text="Open Lidar file", command=self.open_lidar_file)
        radar_button = Button(
            self.load_frame, text="Open Radar file", command=self.open_radar_file)

        process_button.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5)
        lidar_button.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5)
        radar_button.grid(row=1, column=0, ipadx=5, ipady=5, padx=5, pady=5)
        exit_button.grid(row=4, column=0, ipadx=5, ipady=5, padx=5, pady=5)

    # Read and process the default lidar and radar files
    def process_default(self):
        self.process_lidar_file("assets/single.lidar")
        self.process_radar_file("assets/single.radar")

    # Open a lidar file dialog box for user selection of file - file is restriced to .lidar types
    def open_lidar_file(self):
        lidar_filename = filedialog.askopenfilename(
            initialdir="/", title="Open Lidar File", filetypes=[("lidar files", ".lidar")])
        self.process_lidar_file(lidar_filename)

    # Open a radar file dialog box for user selection of file - file is restriced to .radar types
    def open_radar_file(self):
        radar_filename = filedialog.askopenfilename(
            initialdir="/", title="Open Radar File", filetypes=[("radar files", "*.radar")])
        self.process_radar_file(radar_filename)

    # Process the lidar file

    def process_lidar_file(self, lidar_filename):
        lidar_label = Label(
            self.load_frame, text=os.path.basename(lidar_filename))
        lidar_label.grid(row=0, column=1)
        if not lidar_filename:
            return
        try:
            with open(lidar_filename, 'r') as f:
                reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
                for row in reader:
                    rowlist = []
                    for value in row:
                        rowlist.append(int(value))
                    self.lidar_data.append(rowlist)
                self.is_lidar_loaded = True
                self.plot_data()
        except Exception as e:
            print('Unable to open file: %r' % lidar_filename, e)

    # Process the radar file
    def process_radar_file(self, radar_filename):
        radar_label = Label(
            self.load_frame, text=os.path.basename(radar_filename))
        radar_label.grid(row=1, column=1)
        if not radar_filename:
            return
        try:
            with open(radar_filename, 'r') as f:
                reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
                for row in reader:
                    rowlist = []
                    for value in row:
                        rowlist.append(int(value))
                    self.radar_data.append(rowlist)
                self.is_radar_loaded = True
                self.process_data()
                self.plot_data()
        except Exception as e:
            print('Unable to open file: %r' % radar_filename, e)

# ******************************************************

    def process_data(self):
        # populate berg data list with agents to capture lidar and radar information at each x,y location
        for i in range(len(self.radar_data)):
            for j in range(len(self.radar_data[i])):
                radar_value = self.radar_data[i][j]
                lidar_value = self.lidar_data[i][j]
                self.berg_data.append(areaElementAgent.SeaAgent(j, i, radar_value, lidar_value))
        
        # Iterate throught berg agent and generate stuff! 
        for i in range(len(self.berg_data)):

            if(self.berg_data[i].is_ice()):
                print("Is ice?: " + str(self.berg_data[i].is_ice()))
                print("Height above SL: " + str(self.berg_data[i].calculate_height_as()))


# ******************************************************
    # Draw the plot of the lidar and radar files
    def plot_data(self):
        if (self.is_radar_loaded & self.is_lidar_loaded):
            plt.xlim(0, 299)
            plt.ylim(0, 299)

            # Create radar subplot
            plt.subplot(2, 2, 1)
            plt.title("Radar Data")
            plt.imshow(self.radar_data, cmap='Purples',
                       vmin=0, vmax=255, alpha=1)
            plt.colorbar(shrink=0.8)
            plt.xlabel('Metres')
            plt.ylabel('Metres')

            # Create lidar subplot
            plt.subplot(2, 2, 2)
            plt.title("Lidar Data")
            plt.imshow(self.lidar_data, cmap='Greens',
                       vmin=0, vmax=255, alpha=1)
            plt.colorbar(shrink=0.8)
            plt.xlabel('Metres')
            plt.ylabel('Metres')

            # plt.subplot(2, 2, 3)
            # plt.title("Analysis Data")
            # plt.imshow(self.lidar, cmap='Blues', vmin=0, vmax=255, alpha=1)
            # plt.colorbar()
            # Draw the canvas
            self.canvas.draw()


root = Tk()
my_app = MainApplication(root)
root.mainloop()
