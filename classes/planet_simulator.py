import sys
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtCore import QTimer
from classes.celestial_body import CelestalBody
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
from PIL import Image
import math
from utils.constants import *


class PlanetSimulator(QOpenGLWidget):
    def __init__(self, parent=None):
        super(PlanetSimulator, self).__init__(parent)
        self.background = CelestalBody(0, 30, [0, 0, 0])
        self.sun = CelestalBody(100, 4, [0, 0, 0])
        self.earth = CelestalBody(1, 1, [0, 6, 0])

        # Initialize QTimer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)  # Connect the timeout signal to the onTimeout method
        self.timer.start(10)  # Set the timer to call onTimeout every 100 ms (10 times per second)
        self.time_elapsed = 0.00001

        self.planet_texture_id = None
        self.background_texture_id = None
        self.sun_texture_id = None

        self.camera_distance = 10  # Ustawienie początkowej pozycji kamery
        self.camera_angle_x = 90  # Kąt obrotu kamery wokół osi X
        self.camera_angle_y = 0  # Kąt obrotu kamery wokół osi Y
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.mouse_dragging = False

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

        # Load textures
        self.planet_texture_id = self.loadTexture(texture_earth)
        self.background_texture_id = self.loadTexture(texture_background)
        self.sun_texture_id = self.loadTexture(texture_sun)

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
        gluPerspective(50.0, w / float(h), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Ustaw kamerę w oparciu o obrót kamery
        glTranslatef(0.0, 0.0, -self.camera_distance)  # Użyj zmiennej camera_distance
        glRotatef(self.camera_angle_x, 1.0, 0.0, 0.0)  # Obrót wokół osi X
        glRotatef(self.camera_angle_y, 0.0, 1.0, 0.0)  # Obrót wokół osi Y

        # # Renderuj skysferę jako tło
        # glBindTexture(GL_TEXTURE_2D, self.background_texture_id)
        # self.background.drawSphere(self.background.radius, 40, 40)  # Duża sfera otaczająca scenę

        # Render a sun at the center of a plane
        glBindTexture(GL_TEXTURE_2D, self.sun_texture_id)
        self.sun.drawSphere(self.sun.radius, 50, 50)

        # Move the planet to its current position
        glPushMatrix()  # Save the current matrix
        glTranslatef(self.earth.sphere_position[0], self.earth.sphere_position[1], self.earth.sphere_position[2])  # Move sphere
        glBindTexture(GL_TEXTURE_2D, self.planet_texture_id)
        self.earth.drawSphere(self.earth.radius, 50, 50)  # Draw the planet
        glPopMatrix()  # Restore the previous matrix

        self.earth.drawTrail()

    def update_position(self):
        # Update the position of the sphere
        self.time_elapsed += 0.01
        radius = self.earth.radius
        self.earth.sphere_position[0] = 20 * radius * math.cos(self.time_elapsed)
        self.earth.sphere_position[1] = 20 * radius * math.sin(self.time_elapsed)
        self.earth.sphere_position[2] = 0

        #zprint(self.earth.sphere_position)

        self.earth.trail.append(list(self.earth.sphere_position))

        self.update()  # Update the view


    # Obsługa myszy
    def mousePressEvent(self, event):
        self.mouse_dragging = True
        self.last_mouse_x = event.x()
        self.last_mouse_y = event.y()

    def mouseMoveEvent(self, event):
        if self.mouse_dragging:
            dx = event.x() - self.last_mouse_x
            dy = event.y() - self.last_mouse_y

            # Aktualizacja kąta kamery w oparciu o ruch myszy
            self.camera_angle_x += dy * 0.2
            self.camera_angle_y += dx * 0.2

            self.last_mouse_x = event.x()
            self.last_mouse_y = event.y()

            self.update()  # Zaktualizowanie sceny

    def mouseReleaseEvent(self, event):
        self.mouse_dragging = False

    def wheelEvent(self, event):
        # Obsługa kółka myszy - przybliżanie i oddalanie
        zoom_factor = event.angleDelta().y() / 120  # Standardowy skok kółka myszy to 120 jednostek
        self.camera_distance -= zoom_factor  # Zmniejsz lub zwiększ dystans kamery
        self.camera_distance = max(2, self.camera_distance)  # Ograniczenie, by nie przybliżać zbyt blisko
        self.camera_distance = min(60, self.camera_distance)
        self.update()
