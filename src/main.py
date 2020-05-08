""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Assignment: 2 - White Star Line
Author: Javid Yousaf
Student id: 201385963
Date: 15/05/2020

Description: Main script to execute the analysis on the icebergs
"""
from tkinter import Tk
from tkinter import Label
from tkinter import filedialog
from tkinter import Button
import matplotlib.pyplot
import operator
import random
import csv
import os

root = Tk()
root.title("White Star Line Analysis")
root.wm_iconbitmap('assets/iceberg.ico')
root.geometry("500x400")
lidar = []
radar = []
is_radar_loaded = False
is_lidar_loaded = False

# Open a lidar file dialog box and process file


def open_lidar():
    global is_lidar_loaded
    lidar_filename = filedialog.askopenfilename(
        initialdir="/", title="Open Lidar File", filetypes=[("lidar files", ".lidar"), ("all files", ".*")])  # maybe just restrict to .lidar only
    lidar_label = Label(root, text=os.path.basename(lidar_filename))
    lidar_label.pack()
    if not lidar_filename:
        return
    try:
        with open(lidar_filename, 'r') as f:
            reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                rowlist = []
                for value in row:
                    rowlist.append(value)
                lidar.append(rowlist)
            is_lidar_loaded = True
            plot_data()
    except Exception as e:
        print('Unable to open file: %r' % lidar_filename, e)


def open_radar():
    global is_radar_loaded
    radar_filename = filedialog.askopenfilename(
        initialdir="/", title="Open Radar File", filetypes=[("radar files", "*.radar"), ("all files", ".*")])  # maybe just restrict to .radar only
    radar_label = Label(root, text=os.path.basename(radar_filename))
    radar_label.pack()
    if not radar_filename:
        return
    try:
        with open(radar_filename, 'r') as f:
            reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                rowlist = []
                for value in row:
                    rowlist.append(value)
                radar.append(rowlist)
            is_radar_loaded = True
            plot_data()
    except Exception as e:
        print('Unable to open file: %r' % radar_filename, e)


def plot_data():

    if (is_radar_loaded & is_lidar_loaded):
        matplotlib.pyplot.xlim(0, 299)
        matplotlib.pyplot.ylim(0, 299)
        matplotlib.pyplot.imshow(radar)
        matplotlib.pyplot.imshow(lidar)
        matplotlib.pyplot.show()


lidar_button = Button(root, text="Open Lidar file", command=open_lidar)
radar_button = Button(root, text="Open Radar file", command=open_radar)
lidar_button.pack()
radar_button.pack()


root.mainloop()
