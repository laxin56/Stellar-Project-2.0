from ursina import *

class Star:

    def __init__(self, mass, eccentricity, semi_major_axis, scale, texture_path):
        mass = mass
        eccentricity = eccentricity
        semi_major_axis = semi_major_axis
        object = Entity(model="sphere", texture=texture_path, scale=10, position=(0, 0, 0))