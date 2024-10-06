from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton
from classes.planet_simulator import PlanetSimulator
from PyQt5.Qt3DCore import QEntity

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Simulation")
        self.gl_widget = PlanetSimulator(self)
        self.setGeometry(100, 100, 800, 600)
        self.setCentralWidget(self.gl_widget)
        # self.layout = QVBoxLayout(self.gl_widget)
        #
        # self.layout.addWidget(self.gl_widget)
        #
        # self.button_start = QPushButton("Start Simulation")
        # self.button_start.clicked.connect(self.start_simulation)
        # self.layout.addWidget(self.button_start)
        #
        # self.button_stop = QPushButton("Stop Simulation")
        # self.button_stop.clicked.connect(self.stop_simulation)
        # self.layout.addWidget(self.button_stop)

    def start_simulation(self):
        # Add simulation logic here
        self.opengl_widget.timer.start(100)  # Update position every 10 milliseconds

    def stop_simulation(self):
        self.opengl_widget.timer.stop()
