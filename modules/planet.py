import numpy as np
import pandas as pd
from ursina import *
from . import constants
import math

planets_df = pd.read_csv(r'Planets_Parameters.csv', index_col='Parameters')

class Planet:


    def __init__(self, object_name, mass, eccentricity, semi_major_axis, scale, tilt_z, texture_path):
        self.object_name = object_name
        self.mass = mass
        self.eccentricity = eccentricity
        self.semi_major_axis = semi_major_axis
        self.year_time = (2 * np.pi * np.sqrt((pow(self.semi_major_axis, 3) / constants.STD_GRAVITY_PARAMETER))) / (24 * 3600) # year time period for this object in earth days
        self.time = 0
        self.mean = 0
        self.true_anomaly = 0
        self.cos_f = 0
        self.sin_f = 0
        self.x = 0
        self.y = 0
        self.flag_elipse_drawed = False
        self.rotation_period = (planets_df.loc['Rotation Period'][object_name])/24   # Rotation period in hours
        self.tilt_z = tilt_z
        self.object = Entity(model="sphere", texture=texture_path, scale=scale, position=(0, 0, 0), rotation=(0, 0, 20))
        self.orbit_points = []



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

    def Move_Scene(self):
        if self.flag_elipse_drawed != True:
            self.Draw_Elipse()
        else:
            self.Calculate_Position()


    def Calculate_Position(self):
        if self.time > self.year_time:
            self.time = 0
        else:
            self.time += constants.TIME_SCALE*1.0

        self.Mean()
        self.Fixed_Point()
        self.Angle_Calculations()

        r = (self.semi_major_axis * (1 - pow(self.eccentricity,2))) / (1 + self.eccentricity * self.cos_f)
        self.x = r*self.cos_f
        self.y = r*self.sin_f

        self.object.position = (self.x/10**10, (math.tan(math.radians(constants.Coll_Inclination[self.object_name]))*self.x)/10**10, self.y/10**10)
        # self.object.world_rotation_z += (0, (self.rotation_period / 24) * 360 * constants.TIME_SCALE, 0)

    def Draw_Elipse(self):
        for x in range(0, int(self.year_time)+1):
            self.time = x
            self.Mean()
            self.Fixed_Point()
            self.Angle_Calculations()

            r = (self.semi_major_axis * (1 - pow(self.eccentricity, 2))) / (1 + self.eccentricity * self.cos_f)
            self.x = r * self.cos_f
            self.y = r * self.sin_f
            self.orbit_points.append(Vec3(self.x / 10 ** 10,
                                          (math.tan(math.radians(constants.Coll_Inclination[self.object_name])) * self.x) / 10 ** 10,
                                          self.y / 10 ** 10))

        Entity(model=Mesh(vertices=self.orbit_points, mode='line'))
        self.flag_elipse_drawed = True








