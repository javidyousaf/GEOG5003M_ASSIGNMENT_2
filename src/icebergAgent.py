""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Assignment: 2 - White Star Line
Author: Javid Yousaf
Student id: 201385963
Date: 15/05/2020

Description: Class to store and calculate information about an iceberg.
"""


class Iceberg:
    def __init__(self, volume_as, mass_as):
        self._volume_as = volume_as
        self._mass_as = mass_as

    # Getters and Setters for class properties
    def get_volume_as(self):
        return self._volume_as

    def set_volume_as(self, value):
        self._volume_as = value

    def get_mass_as(self):
        return self._mass_as

    def set_mass_as(self, value):
        self._mass_as = value


    # calculated functions
    def get_total_volume(self):
        return self._volume_as * 10

    def get_total_mass(self):
        return self._mass_as * 10

    def is_towable(self):
        self.get_total_mass() < 36000000
