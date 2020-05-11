""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Assignment: 2 - White Star Line
Author: Javid Yousaf
Student id: 201385963
Date: 15/05/2020

Description: Class to capture and calculate information about each element 
"""

class SeaAgent:
    def __init__(self, x, y, radar_value, lidar_value):
        self._y = x # x coord of element in the area matrix
        self._x = y # y coord of element in the area matrix
        self._radar_value = radar_value # radar value at the coord.
        self._lidar_value = lidar_value # radar value at the coord.


    # Getters and Setters for class properties
    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

    def get_radar_value(self):
        return self._radar_value

    def set_radar_value(self, value):
        self._radar_value = value

    def get_lidar_value(self):
        return self._lidar_value

    def set_lidar_value(self, value):
        self._lidar_value = value

    def is_ice(self):
        return self._radar_value > 99

    def calculate_height_as(self):
        if (self._lidar_value > 0):
            return self._lidar_value / 10
        else:
            return 0