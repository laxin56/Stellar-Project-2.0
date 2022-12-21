from ursina import *

class Star:

    def __init__(self, mass, eccentricity, semi_major_axis, texture_path):
        mass = mass
        eccentricity = eccentricity
        semi_major_axis = semi_major_axis
        object = Entity(model="sphere", texture=texture_path, scale=1.5, position=(0, 0, 0))