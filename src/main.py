""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Assignment: 2 - White Star Line
Author: Javid Yousaf
Student id: 201385963
Date: 15/05/2020

Description: Main application for the White Star Line analysis.
Contains funtionality to load, process, display and export the analysis. 
"""

import elementAgent
import icebergAgent
from datetime import datetime
from tkinter import Tk, Label, Button, filedialog, Menu, Frame, LabelFrame, ttk
import os
import sys
import csv
import operator
import enum
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


# class Style(enum.Enum):
#     PAD_X = 5
#     PAD_Y = 5
#     IPAD_X = 5
#     IPAD_Y = 5


# Define a main application class to set up the GUI layout and interaction
class MainApplication:
    '''
    Main application for the White Star Line analysis.
    Contains funtionality to load, process, display and export the analysis. 
    '''
    def __init__(self, master):
        '''
        Initialise the application by setting up and laying out the GUI elements.
        '''
        self.master = master
        master.title("White Star Line Analysis")
        master.wm_iconbitmap('assets/iceberg.ico')
        master.geometry("1150x650+10+10")
        master.resizable(width=False, height=False) # disable resizing of main window

        self.lidar_data = []
        self.radar_data = []

        self.area_elements = []  # list to store the are element agents
        self.icebergs = []  # list to store the identified icebergs agents

        self.is_radar_loaded = False
        self.is_lidar_loaded = False

        self.canvas = None

        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Default Processing",
                             command=self.process_default)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        filemenu.add_command(label="Restart", command=self.restart_app)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)


        # Overide the default X button to quit the application gracefully
        master.protocol("WM_DELETE_WINDOW", master.quit)

        # main application panels
        buttonPane = Frame(master)
        self.chartPane = Frame(master)
        buttonPane.grid(row=0,column=0, sticky="nsew")
        self.chartPane.grid(row=0,column=1, sticky="nsew")

        master.grid_columnconfigure(0, weight=1, uniform="x")
        master.grid_columnconfigure(1, weight=2, uniform="x")

        self.fig_analysis = plt.figure(figsize=(7, 5))

        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.fig_analysis, master=self.chartPane)
        self.canvas._tkcanvas.grid(row=0, column=0, padx=10, pady=10)

        self.process_frame = LabelFrame(buttonPane, text="Default Processing")
        self.process_frame.grid(row=0, column=0, ipadx=5,ipady=5, padx=5, pady=5, sticky="W")

        self.divider_1 = ttk.Separator(buttonPane, orient="horizontal")
        self.divider_1.grid(row=1, column=0, ipadx=5,ipady=5, padx=5, pady=5, sticky="ew")

        self.load_frame = LabelFrame(buttonPane, text="Manual File Load")
        self.load_frame.grid(row=2, column=0, ipadx=5,ipady=5, padx=5, pady=5, sticky="W")

        self.result_frame = LabelFrame(buttonPane, text="Iceberg Analysis")
        self.result_frame.grid(row=3, column=0, ipadx=5,ipady=5, padx=5, pady=5, sticky="W")

        self.button_frame = LabelFrame(buttonPane, text="Controls")
        self.button_frame.grid(row=4, column=0, ipadx=5,ipady=5, padx=5, pady=5, sticky="W")
        
        process_button = Button(self.process_frame, text="Run Process >>", command=self.process_default)
        process_button.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        lidar_button = Button(self.load_frame, text="Open Lidar file", command=self.open_lidar_file)
        lidar_button.grid(row=1, column=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        radar_button = Button(self.load_frame, text="Open Radar file", command=self.open_radar_file)
        radar_button.grid(row=2, column=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        # Results panel
        # Headings
        total_volume_as_label = Label(self.result_frame, text="Total Volume above sea level (m\u00B3)")
        total_volume_as_label.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        total_mass_as_label = Label(self.result_frame, text="Total Mass above sea level (kg)")
        total_mass_as_label.grid(row=1, column=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        total_volume_label = Label(self.result_frame, text="Total Volume of iceberg (m\u00B3)")
        total_volume_label.grid(row=2, column=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        total_mass_as_label = Label(self.result_frame, text="Total Mass of iceberg (kg)")
        total_mass_as_label.grid(row=3, column=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        tow_decision_label = Label(self.result_frame, text="Result")
        tow_decision_label.grid(row=4, column=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        # result values
        self.total_volume_as_result_label = Label(self.result_frame, text="n/a")
        self.total_volume_as_result_label.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        self.total_mass_as_result_label = Label(self.result_frame, text="n/a")
        self.total_mass_as_result_label.grid(row=1, column=1, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        self.total_volume_result_label = Label(self.result_frame, text="n/a")
        self.total_volume_result_label.grid(row=2, column=1, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        self.total_mass_result_label = Label(self.result_frame, text="n/a")
        self.total_mass_result_label.grid(row=3, column=1, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        self.tow_decision_result_label = Label(self.result_frame, text="n/a")
        self.tow_decision_result_label.grid(row=4, column=1, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        # Control button panel
        export_button = Button(self.button_frame, text='Export to file', command=self.export_analysis_file)
        export_button.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

        clear_button = Button(self.button_frame, text='Clear Data', command=self.clear_app_data)
        clear_button.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")
        
        exit_button = Button(self.button_frame, text='Exit', command=master.quit)
        exit_button.grid(row=0, column=2, ipadx=5, ipady=5, padx=5, pady=5, sticky="W")

    def process_default(self):
        '''
        Read and process the default lidar and radar files for a single iceberg.
        '''
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
        lidar_label = Label(self.load_frame, text=os.path.basename(lidar_filename))
        lidar_label.grid(row=1, column=1)
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
        radar_label.grid(row=2, column=1)
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


    def process_data(self):
        # check if radar and lidar data have the same size grids:
        radar_row_count = len(self.radar_data)
        radar_column_count = len(self.radar_data[0])
        lidar_row_count = len(self.lidar_data)
        lidar_column_count = len(self.lidar_data[0])

        if (radar_row_count == lidar_row_count & radar_column_count == lidar_column_count):
            rows = radar_row_count
            columns = radar_column_count
            # populate berg data list with agents to capture lidar and radar information at each x,y location
            for i in range(rows):
                for j in range(columns):
                    radar_value = self.radar_data[i][j]
                    lidar_value = self.lidar_data[i][j]
                    self.area_elements.append(elementAgent.AreaElement(j, i, radar_value, lidar_value))

            # Iterate throught berg agent and generate iceberg data
            total_volume_as = 0
            total_mass_as = 0

            for i in range(len(self.area_elements)):
                if(self.area_elements[i].is_ice()):
                    element_height_as = (self.area_elements[i].calculate_height_as())

                    # As each element is 1m x 1m the volume of ice above sea level will be 1 x 1 x height_as
                    # which is just height_as but we calculate and assign a variable for clarity:
                    element_volume_as = 1 * 1 * element_height_as
                    total_volume_as += element_volume_as

                    # Density of ice is approx 900 Kg/m3 therefore mass is 900 x volume:
                    element_mass_as = 900 * element_volume_as
                    total_mass_as += element_mass_as

            self.icebergs.append(icebergAgent.Iceberg(total_volume_as, total_mass_as))
            self.display_iceberg_analysis()

    # Display iceberg data - iterate through the list of stored icebergs and get relevant data
    def display_iceberg_analysis(self):
        for i in range(len(self.icebergs)):
            self.total_volume_as_result_label['text'] = str(self.icebergs[i].get_volume_as()) + " m\u00B3"
            self.total_mass_as_result_label['text'] = str(self.icebergs[i].get_mass_as()) + " Kg"
            self.total_volume_result_label['text'] = str(self.icebergs[i].get_total_volume()) + " m\u00B3"
            self.total_mass_result_label['text'] = str(self.icebergs[i].get_total_mass()) + " Kg"

            if (self.icebergs[i].is_towable()):
                self.tow_decision_result_label['text'] = "Iceberg CAN be towed."
                self.tow_decision_result_label['bg'] = "green"
                self.tow_decision_result_label['foreground'] = "white"
            else:
                self.tow_decision_result_label['text'] = "Iceberg is NOT towable."
                self.tow_decision_result_label['bg'] = "red"
                self.tow_decision_result_label['foreground'] = "white"

    def export_analysis_file(self):
        '''
        Export iceberg analysis data to a text file - 
        this will display a file dialog and allow the user the enter a file name and 
        choose a location to save the file.
        '''
        date_time_obj = datetime.now()
        time_stamp = date_time_obj.strftime("%y%m%d%H%M%S%f")

        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        f.write("Iceberg Analysis\n\n")
        for i in range(len(self.icebergs)):
            f.write("Total mass above sea level: " + str(self.icebergs[i].get_mass_as()) + " kg\n")
            f.write("Total volume above sea level: " + str(self.icebergs[i].get_volume_as()) + " m3\n")
            f.write("Total mass: " + str(self.icebergs[i].get_total_mass()) + " kg\n")
            f.write("Total volume: " + str(self.icebergs[i].get_total_volume()) + " m3\n")
            if (self.icebergs[i].is_towable()):
                f.write("This iceberg CAN be towed.\n")
            else:
                f.write("This iceberg is NOT towable.\n")
        f.write("\n")
        f.write("Created: " + time_stamp)
        f.close()

    def clear_app_data(self):
        self.lidar_data = []
        self.radar_data = []
        self.area_elements = []
        self.icebergs = []
        self.is_radar_loaded = False
        self.is_lidar_loaded = False
        self.total_volume_as_result_label['text'] = "n/a"
        self.total_mass_as_result_label['text'] = "n/a"
        self.total_volume_result_label['text'] = "n/a"
        self.total_mass_result_label['text'] = "n/a"

        self.tow_decision_result_label['text'] = "n/a"
        self.tow_decision_result_label['bg'] = "lightgray"
        self.tow_decision_result_label['foreground'] = "black"

        self.fig_analysis = plt.figure(figsize=(7, 5))
        self.canvas._tkcanvas.destroy()
        self.canvas = None
        self.canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(self.fig_analysis, master=self.chartPane)
        self.canvas._tkcanvas.grid(row=0, column=0, padx=10, pady=10)

    def restart_app(self):
        """
        Restarts the application.
        Note: this function does not save any data already generated.
         Analysis data can be exported before calling this function.
        """
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    
    # Draw the plot of the lidar and radar files
    def plot_data(self):
        if (self.is_radar_loaded & self.is_lidar_loaded):
            plt.xlim(0, 299)
            plt.ylim(0, 299)

            # Create radar subplot
            plt.subplot(2, 2, 1)
            plt.title("Radar Data")
            plt.imshow(self.radar_data, cmap='Purples', vmin=0, vmax=255, alpha=1)
            plt.colorbar()
            plt.xlabel('Metres')
            plt.ylabel('Metres')

            # Create lidar subplot
            plt.subplot(2, 2, 2)
            plt.title("Lidar Data")
            plt.imshow(self.lidar_data, cmap='Greens', vmin=0, vmax=255, alpha=1)
            plt.colorbar()
            plt.xlabel('Metres')
            plt.ylabel('Metres')

            self.canvas.draw()

root = Tk()
my_app = MainApplication(root)
root.mainloop()
