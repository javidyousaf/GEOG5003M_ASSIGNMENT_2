
<img  align="left" src="src\assets\images\wsl.ico" alt="Whistlerpro / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)" width="180" height="180">

# White Star Line Analysis

###  White Start Line Analysis is a desktop application developed to detect and analyse icebergs, using satellite lidar and radar data of an arear of the sea in the White Start Line shipping lanes. The analysis calculates the volume and mass of the iceberg to determine its tow ability.

## Contents

1. [Application screenshot](#application-screenshot)
1. [Development tools](#development-tools)
1. [Installation](#installation)
1. [User guide](#user-guide)
1. [Documents](#documents)
1. [Developer Information](#developer-information)
1. [License](#license)
1. [Attribution](#attribution)

## Application Screenshot

<img src="src\assets\images\wsl_screen_grab.png" alt="White Star Line Analysis main window" width="1000" height="600">

## Development Tools

This application was developed using the following software tools:

* [Python 3.8.2](https://www.python.org/downloads/).
* Visual Studio Code with Microsoft Python extension.
* Git version 2.25.1 for Windows. [Git downloads](https://git-scm.com/downloads).

## Installation

* Install Python 3.8.2 or higher.
* Clone the repository by typing the following in a command window:<pre><code>git clone https://github.com/javidyousaf/GEOG5003M_ASSIGNMENT_2.git</code></pre>
* In a command or bash window navigate to the **src** folder in the repository that you just cloned and run the application:<pre><code>cd src 
python main.py</code></pre>

## User Guide
The application allows the user to load  ***radar*** and ***lidar*** file of a geographical area of sea. It then processes this data and detects icebergs and calculates the volume and mass above sea level and an estimation of the total volume and mass. It determines if the iceberg is towable and displays this information.

<table>
    <tr>
        <td width="350"><img src="src\assets\images\default_button.PNG" alt="Default button" width="220" height="120"></td>
        <td>
            <h3>Default processing</h3>
            The <b>Run Process</b> button automates the processing by loading the radar and lidar files automatically and then processing them and displaying the analysis and charts in the chart panel.
        </td>
    </tr>
    <tr>
        <td width="350"><img src="src\assets\images\manual_buttons.PNG" alt="Manual processing" width="220" height="120"></td>
        <td>
            <h3>Manual processing</h3>
            The <b>Manual Processing</b> allows the user to select a <i>lidar</i> and <i>radar</i> file from the desktop file system. When both files are loaded the application will automatically process them and display the analysis and charts.
        </td>
    </tr>
    <tr>
        <td width="350"><img src="src\assets\images\manual_selected.PNG" alt="Manual select" width="220" height="120"></td>
        <td>
            <h3>Loading a file</h3>
            The file selection dialog will open and only allow the selection of a <i>.lidar</i> or <i>.radar</i> file type. Once selected the loaded file name displays next to the button.
        </td>
    </tr>
    <tr>
        <td width="350"><img src="src\assets\images\analysis.PNG" alt="Results of analysis" width="320" height="200"></td>
        <td>
            <h3>Analysis and Results</h3>
            The <b>Iceberg Analysis</b> panel shows the results of the analysis by displaying the volume and mass above sea level and total volume and mass. If the iceberg is towable (i.e. if the total mass is less than 36 million kgs) then this is indicated and displayed in green. If not towable then the message is displayed in red.
        </td>
    </tr>
    <tr>
        <td width="350"><img src="src\assets\images\control_buttons.PNG" alt="Results of analysis" width="320" height="100"></td>
        <td>
            <h3>Control Buttons</h3>
            <b>Export to file</b> button will open a file dialog and allow the user to select a location and filename to save a simple text file containing the analysis results.</br>
            <b>Clear Data</b> button unloads the loaded files and clears the charts and analysis ready to load new data for processing.</br>
            <b>Exit</b> button closes the application window.
        </td>
    </tr>
</table>

***Note:*** This application is limited to analysing a single iceberg. Future development will include the ability to analyse an area of sea with multiple icebergs.

## Documents
The software development guide can be viewed as a pdf [here](documents\WhiteStarLineSoftwareDevelopmentGuide.pdf).
## Developer Information
Code developed by [Javid Yousaf](https://github.com/javidyousaf/) for University of Leeds MSc Geographical Information Science course. 

Module GEOG5003M - Programming for Geographical Information Analysis.

## License

This software is licensed under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007. 

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Attribution

White Star Line logo. Whistlerpro / CC BY-SA (https://creativecommons.org/licenses/by-sa/3.0)
