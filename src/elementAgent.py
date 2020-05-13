""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Assignment: 2 - White Star Line
Author: Javid Yousaf
Student id: 201385963
Date: 15/05/2020
version: 1.0

Description: Class to capture and calculate information about each element 
"""


class AreaElement:
    '''
    Captures the combined information from lidar and radar data at a single
    point in the area grid.
    '''

    def __init__(self, x, y, radar_value, lidar_value):
        '''
        To store data about the area element.
        The class is initailsed by providing the x, y coords and
        the radar and lidar vlaues at these coords.
        '''
        self._y = x
        self._x = y
        self._radar_value = radar_value
        self._lidar_value = lidar_value 

    ''' Getters and Setters to set and access class properties safely '''

    def get_x(self):
        ''' get x coord of element in the area matrix '''
        return self._x

    def set_x(self, value):
        ''' set x coord of element in the area matrix '''
        self._x = value

    def get_y(self):
        ''' get y coord of element in the area matrix '''
        return self._y

    def set_y(self, value):
        ''' set y coord of element in the area matrix '''
        self._y = value

    def get_radar_value(self):
        ''' get radar value of element in the area matrix '''
        return self._radar_value

    def set_radar_value(self, value):
        ''' set radar value of element in the area matrix '''
        self._radar_value = value

    def get_lidar_value(self):
        ''' get lidar value of element in the area matrix '''
        return self._lidar_value

    def set_lidar_value(self, value):
        ''' set lidar value of element in the area matrix '''
        self._lidar_value = value

    '''
    Calculated functions to provide additional data for the iceberg
    '''

    def is_ice(self):
        '''
        Determine if the element is ice.
        Returns True if the element value is 100 or more.
        Returns False if the element value is leass than 100.
         '''
        return self._radar_value > 99

    def calculate_height_as(self):
        '''
        Calculates the elements height in metres above sea level.
         '''
        if (self._lidar_value > 0):
            return self._lidar_value / 10
        else:
            return 0
