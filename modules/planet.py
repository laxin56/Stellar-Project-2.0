import numpy as np
from ursina import *
#import constants
SUN_MASS = 1.989*(pow(10,30))      # Sun mass
GRAVITY_CONSTANT = 6.67408/pow(10,11)    # Gravity constant
STD_GRAVITY_PARAMETER = GRAVITY_CONSTANT*SUN_MASS
class Planet:

    def __init__(self, mass, eccentricity, semi_major_axis, scale, texture_path):
        self.mass = mass
        self.eccentricity = eccentricity
        self.semi_major_axis = semi_major_axis
        self.year_time = (2 * np.pi * np.sqrt((pow(self.semi_major_axis, 3) / STD_GRAVITY_PARAMETER))) / (24 * 3600) # year time period for this object in earth days
        self.time = 0
        self.mean = 0
        self.true_anomaly = 0
        self.cos_f = 0
        self.sin_f = 0
        self.x = 0
        self.y = 0
        self.object = Entity(model="sphere", texture=texture_path, scale=scale, position=(0, 0, 0))


    def Mean(self):
        self.mean = (self.time * 2 * np.pi) / self.year_time

    def Fixed_Point(self):
        E = self.mean + self.eccentricity * np.sin(self.mean)
        i = 0
        while(True):
            i += 1
            p_E = E
            E = self.mean + self.eccentricity * np.sin(p_E)
            if np.abs(p_E - E) < 0.000001:
                self.true_anomaly = E
                break

    def Angle_Calculations(self):
        self.cos_f = (np.cos(self.true_anomaly) - self.eccentricity) / (1 - self.eccentricity * np.cos(self.true_anomaly))
        self.sin_f = (np.sqrt(1 - pow(self.eccentricity, 2)) * np.sin(self.true_anomaly)) / (1 - self.eccentricity * np.cos(self.true_anomaly))

    def Calculate_Position(self):
        if self.time > self.year_time:
            self.time = 0
        else:
            self.time += 1.0

        self.Mean()
        self.Fixed_Point()
        self.Angle_Calculations()

        r = (self.semi_major_axis * (1 - pow(self.eccentricity,2))) / (1 + self.eccentricity * self.cos_f)
        self.x = r*self.cos_f
        self.y = r*self.sin_f

        self.object.position = (self.x/10**10, self.y/10**10, 0)