from OpenGL.GL import *
import numpy as np
from PIL import Image
import math
from utils.constants import *

class CelestalBody:
    def __init__(self, name, mass, radius, initial_position):
        self.planet_texture_id = None
        self.background_texture_id = None

        self.mass = mass
        self.radius = radius
        self.sphere_position = initial_position
        self.trail = []

        self.object_name = name
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
        self.rotation_period = 365   # Rotation period in hours
        self.tilt_z = tilt_z

        def mean(self):
            self.mean = (self.time * 2 * np.pi) / self.year_time

        def fixed_point(self):
            E = self.mean + self.eccentricity * np.sin(self.mean)
            i = 0
            while(True):
                i += 1
                p_E = E
                E = self.mean + self.eccentricity * np.sin(p_E)
                if np.abs(p_E - E) < 0.000001:
                    self.true_anomaly = E
                    break

        def angle_calculations(self):
            self.cos_f = (np.cos(self.true_anomaly) - self.eccentricity) / (1 - self.eccentricity * np.cos(self.true_anomaly))
            self.sin_f = (np.sqrt(1 - pow(self.eccentricity, 2)) * np.sin(self.true_anomaly)) / (1 - self.eccentricity * np.cos(self.true_anomaly))

        def calculate_position(self):
            if self.time > self.year_time:
                self.time = 0
            else:
                self.time += TIME_SCALE*1.0

            self.mean()
            self.fixed_Point()
            self.angle_calculations()

            r = (self.semi_major_axis * (1 - pow(self.eccentricity, 2))) / (1 + self.eccentricity * self.cos_f)
            self.x = r*self.cos_f
            self.y = r*self.sin_f

            self.object.position = (self.x/10**10, (math.tan(math.radians(tilt_z))*self.x)/10**10, self.y/10**10)
            # self.object.world_rotation_z += (0, (self.rotation_period / 24) * 360 * constants.TIME_SCALE, 0)
    def drawSphere(self, radius, lats, longs):
        for i in range(lats):
            lat0 = np.pi * (-0.5 + float(i) / lats)
            z0 = np.sin(lat0)
            zr0 = np.cos(lat0)

            lat1 = np.pi * (-0.5 + float(i + 1) / lats)
            z1 = np.sin(lat1)
            zr1 = np.cos(lat1)

            glBegin(GL_QUAD_STRIP)
            for j in range(longs + 1):
                lng = 2 * np.pi * float(j) / longs
                x = np.cos(lng)
                y = np.sin(lng)

                glTexCoord2f(float(j) / longs, float(i) / lats)
                glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)

                glTexCoord2f(float(j) / longs, float(i + 1) / lats)
                glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)
            glEnd()

    def drawTrail(self):
        """Draw the trail (orbit) as a series of lines or points."""
        glBegin(GL_LINE_STRIP)
        for pos in self.trail:
            glVertex3f(pos[0], pos[1], pos[2])  # Draw each position in the trail
        glEnd()
    def loadTexture(self, image_path):
        img = Image.open(image_path)
        img_data = np.array(list(img.getdata()), np.uint8)
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.width, img.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
        return texture_id