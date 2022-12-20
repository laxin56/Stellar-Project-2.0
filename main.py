import numpy as np
import time
from ursina import *

app = Ursina()
# Sky(texture = "sky_default")
window.title = "My Game"
window.color = color.black
camera.position = (0, 0)
window.borderless = False


sun = Entity(model="sphere", color=color.yellow, texture='textures/2k_mercury', scale=2)
earth = Entity(model="sphere", color=color.blue, texture='noise', scale=0.5)
mars = Entity(model="sphere", color=color.red, texture='noise', scale=0.5)


app.run()