""" 
Module: GEOG5003M Programming for Geographical Information Analysis
Assignment: 2 - White Star Line
Author: Javid Yousaf
Student id: 201385963
Date: 15/05/2020
version: 1.0

Description: Class to store and calculate information about an iceberg.
"""


class Iceberg:
    def __init__(self, volume_as, mass_as):
        '''
        To store data about the iceberg.
        The class is initailsed by providing the mass and volume above sea level
        '''
        self._volume_as = volume_as  # volume above sea level
        self._mass_as = mass_as  # mass above sea level

    '''
    Getters and Setters to set and access class properties safely
    '''

    def get_volume_as(self):
        ''' get volume above sea level '''
        return self._volume_as

    def set_volume_as(self, value):
        ''' set volume above sea level '''
        self._volume_as = value

    def get_mass_as(self):
        ''' get mass above sea level '''
        return self._mass_as

    def set_mass_as(self, value):
        ''' set mass above sea level '''
        self._mass_as = value

    '''
    Calculated functions to provide additional data for the iceberg
    '''

    def get_total_volume(self):
        '''
        Calculates the total volume of the iceberg on the assumption that
        90% of the volume is below sea level.
        '''
        return self._volume_as * 10

    def get_total_mass(self):
        '''
        Calculates the total mass of the iceberg on the assumption that
        90% of the mass is below sea level.
        '''
        return self._mass_as * 10

    def is_towable(self):
        '''
        Returns True if the iceberg mass is less than 36 million kg's.
        Returns False if the iceberg mass is 36 million kg's or more.
        '''
        return self.get_total_mass() < 36000000
