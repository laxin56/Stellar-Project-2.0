# from classes.main_window import MainWindow
#
#
# class Scene:
#     def __init__(self, radius: int, mass: float):
#         self._radius = radius
#         self._mass = mass
#         self.window = MainWindow()
#
#     def run(self):
#         self.window.setGeometry(100, 100, 1200, 900)
#         self.window.show()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from PIL import Image


class PlanetSimulator(QOpenGLWidget):
    def __init__(self, parent=None):
        super(PlanetSimulator, self).__init__(parent)
        self.planet_texture_id = None
        self.background_texture_id = None

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        self.planet_texture_id = self.loadTexture('2k_earth_daymap.jpg')
        self.background_texture_id = self.loadTexture('2k_stars_milky_way.jpg')  # Dodaj teksturę tła
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 1.0, 0.1, 100.0)

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

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, w / float(h), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

        # Renderuj tło
        glBindTexture(GL_TEXTURE_2D, self.background_texture_id)
        self.drawBackground()

        # Renderuj sferę (planetę)
        glBindTexture(GL_TEXTURE_2D, self.planet_texture_id)
        self.drawSphere(1, 50, 50)

    def drawBackground(self):
        # Rysowanie prostokąta w tle
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-4.0, -3.0, -5.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(4.0, -3.0, -5.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(4.0, 3.0, -5.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-4.0, 3.0, -5.0)
        glEnd()

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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Planet Simulator with Background")
        self.setGeometry(100, 100, 800, 600)
        self.gl_widget = PlanetSimulator(self)
        self.setCentralWidget(self.gl_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
