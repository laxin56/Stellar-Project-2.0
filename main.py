import numpy as np
import time
from ursina import *
from modules import planet
from modules import star
from modules import constants
import pandas as pd

#Importing a csv file, which stores parameters of planets in Solar System
planets_df = pd.read_csv(r'Planets_Parameters.csv', index_col='Parameters')


app = Ursina()
window.title = "My Game"
window.color = color.black
camera.position = (0, 0, -100)
window.borderless = False
window.fullscreen = False
Sky(texture="/textures/2k_stars.jpg",texture_scale=(2000,2000))

'''
%%% For now it is not needed %%%%

def camera_control():
    if held_keys['q']:  # If q is pressed
        camera.position += (0, 0, 10*time.dt)  # zoom in
    if held_keys['z']:  # If a is pressed
        camera.position -= (0, 0, 10*time.dt)  # zoom out
'''

#Planets for the solar system simulation
sun = star.Star(mass=constants.SUN_MASS,eccentricity=1,semi_major_axis=0,scale=constants.SUN_RADIUS,texture_path='/textures/2k_sun.jpg')
earth = planet.Planet(object_name='Earth',mass=constants.Coll_Mass['Earth'], eccentricity=constants.Coll_Eccentricity['Earth'],semi_major_axis=constants.Coll_SMA['Earth'],tilt_z=planets_df.loc['Obliquity to Orbit']['Earth'], scale=constants.Coll_Radius['Earth'],  texture_path='/textures/2k_earth_daymap.jpg')
mars = planet.Planet(object_name='Mars',mass=constants.Coll_Mass['Mars'], eccentricity=constants.Coll_Eccentricity['Mars'],semi_major_axis=constants.Coll_SMA['Mars'], tilt_z=planets_df.loc['Obliquity to Orbit']['Mars'], scale=constants.Coll_Radius['Mars'], texture_path='/textures/2k_mars.jpg')
venus = planet.Planet(object_name='Venus',mass=constants.Coll_Mass['Venus'], eccentricity=constants.Coll_Eccentricity['Venus'],semi_major_axis=constants.Coll_SMA['Venus'], tilt_z=planets_df.loc['Obliquity to Orbit']['Venus'], scale=constants.Coll_Radius['Venus'], texture_path='/textures/2k_venus.jpg')
mercury = planet.Planet(object_name='Mercury',mass=constants.Coll_Mass['Mercury'], eccentricity=constants.Coll_Eccentricity['Mercury'],semi_major_axis=constants.Coll_SMA['Mercury'], tilt_z=planets_df.loc['Obliquity to Orbit']['Mercury'], scale=constants.Coll_Radius['Mercury'], texture_path='/textures/2k_mercury.jpg')
jupiter = planet.Planet(object_name='Jupiter',mass=constants.Coll_Mass['Jupiter'], eccentricity=constants.Coll_Eccentricity['Jupiter'],semi_major_axis=constants.Coll_SMA['Jupiter'], tilt_z=planets_df.loc['Obliquity to Orbit']['Jupiter'], scale=constants.Coll_Radius['Jupiter'], texture_path='/textures/2k_jupiter.jpg')




def update():
    earth.Move_Scene()
    mars.Move_Scene()
    mercury.Move_Scene()
    venus.Move_Scene()
    jupiter.Move_Scene()

ed = EditorCamera()
app.run()