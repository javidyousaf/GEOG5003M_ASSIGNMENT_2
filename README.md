<table>
    <tr>
        <td><img src="src\assets\images\wsl.ico" alt="Whistlerpro / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)" width="100" height="100"></td>
        <td><h1>White Star Line Analysis</h1></td>
    </tr>
</table>

White Start Line Analysis is a desktop application developed to detect and analyse icebergs and determine their tow ability using satellite lidar and radar data.

## Contents

1. [Application screenshot](#1.-application-creenshot)
1. [Development tools](#2.-development-tools)
1. [Installation](#3.-installation)
1. [User guide](#4.-user-guide)
1. [Developer Information](#5.-developer-information)
1. [License](#6.-license)
1. [Attribution](#7.-attribution)

## 1. Application Screenshot

<img src="src\assets\images\wsl_screen_grab.png" alt="White Star Line Analysis main window" width="1000" height="600">

## 2. Development Tools

This application was developed using the following software tools:

* [Python 3.8.2](https://www.python.org/downloads/).
* Visual Studio Code with Microsoft Python extension.
* Git version 2.25.1 for Windows. [Git downloads](https://git-scm.com/downloads).

## 3. Installation

* Install Python 3.8.2 or higher.
* Clone the repository by typing the following in a command window:<pre><code>git clone https://github.com/javidyousaf/GEOG5003M_ASSIGNMENT_2.git</code></pre>
* In a command or bash window navigate to the **src** folder in the repository that you just cloned and run the application:<pre><code>cd src 
python main.py</code></pre>

## 4. User Guide
The application allows the user to load  ***radar*** and ***lidar*** file of a geographical area of sea. It then processes this data and detects icebergs and calculates the volume and mass above sea level and an estimation of the total volume and mass. It detemines if the iceberg is towable and displays this information.

<table>
    <tr>
        <td><img src="src\assets\images\default_button.PNG" alt="Default button" width="150" height="80"></td>
        <td>
            <h3>Default processing</h3>
            The <b>Run Process</b> button automates the processing by loading the radar and lidar files automatically and then processing them and diplaying the analysis and charts in the chart panel.
        </td>
    </tr>
    <tr>
        <td><img src="src\assets\images\manual_buttons.PNG" alt="Manual processing" width="150" height="80"></td>
        <td>
            <h3>Manual processing</h3>
            The <b>Manual Processsing</b> allows the user to select a <i>lidar</i> and <i>radar</i> file fron the desktop file system. When both files are loaded the appliaction will automatically process them and diplay the analysis and charts.
        </td>
    </tr>
</table>



## 5. Developer Information
Code developed by [Javid Yousaf](https://github.com/javidyousaf/) for University of Leeds MSc Geographical Information Science course. 

Module GEOG5003M - Programming for Geographical Information Analysis.

## 6. License

This software is licensed under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. 

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## 7. Attribution

White Star Line logo. Whistlerpro / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)
