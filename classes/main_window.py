from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton
from classes.planet_simulator import PlanetSimulator
from PyQt5.Qt3DCore import QEntity

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Simulation")
        self.gl_widget = PlanetSimulator(self)
        self.setGeometry(150, 150, 1000, 800)
        self.setCentralWidget(self.gl_widget)

    def start_simulation(self):
        # Add simulation logic here
        self.gl_widget.timer.start(30)  # Update position every 10 milliseconds

    def stop_simulation(self):
        self.opengl_widget.timer.stop()
