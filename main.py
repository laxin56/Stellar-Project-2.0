import numpy as np
import time
from ursina import *
from modules import planet
from modules import star
from modules import constants


app = Ursina()
window.title = "My Game"
window.color = color.black
camera.position = (0, 0)
window.borderless = False
window.fullscreen = True
Sky(texture="/textures/2k_stars.jpg",texture_scale=(600,600))

'''
sun = Entity(model="sphere", color=color.yellow, texture='/textures/2k_sun.jpg', scale=2)
earth = Entity(model="sphere", texture='/textures/2k_earth_daymap.jpg', scale=0.5, position=(3, 0, 0))
mars = Entity(model="sphere", color=color.red, texture='noise', scale=0.5, position=(6, 0, 0))
'''

def camera_control():
    if held_keys['q']:  # If q is pressed
        camera.position += (0, 0, 10*time.dt)  # zoom in
    if held_keys['z']:  # If a is pressed
        camera.position -= (0, 0, 10*time.dt)  # zoom out



sun = star.Star(1,1,1,'/textures/2k_sun.jpg')
earth = planet.Planet(mass=constants.Coll_Mass['Earth'], eccentricity=constants.Coll_Eccentricity['Earth'],semi_major_axis=constants.Coll_SMA['Earth'], scale=constants.Coll_Radius['Earth'],  texture_path='/textures/2k_earth_daymap.jpg')
mars = planet.Planet(mass=constants.Coll_Mass['Mars'], eccentricity=constants.Coll_Eccentricity['Mars'],semi_major_axis=constants.Coll_SMA['Mars'], scale=constants.Coll_Radius['Mars'], texture_path='/textures/2k_mars.jpg')
venus = planet.Planet(mass=constants.Coll_Mass['Venus'], eccentricity=constants.Coll_Eccentricity['Venus'],semi_major_axis=constants.Coll_SMA['Venus'], scale=constants.Coll_Radius['Venus'], texture_path='/textures/2k_venus.jpg')
mercury = planet.Planet(mass=constants.Coll_Mass['Mercury'], eccentricity=constants.Coll_Eccentricity['Mercury'],semi_major_axis=constants.Coll_SMA['Mercury'], scale=constants.Coll_Radius['Mercury'], texture_path='/textures/2k_mercury.jpg')


def update():
    camera_control()
    '''
    if earth.time > earth.year_time:
        earth.time = 0
    else:
        earth.time+=1.0
'''
    earth.Calculate_Position()
    mars.Calculate_Position()
    mercury.Calculate_Position()
    venus.Calculate_Position()


app.run()