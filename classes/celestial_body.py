from OpenGL.GL import *
import numpy as np
from PIL import Image


class CelestalBody:
    def __init__(self, mass, radius, sphere_position):
        self.planet_texture_id = None
        self.background_texture_id = None

        self.mass = mass
        self.radius = radius
        self.sphere_position = sphere_position

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