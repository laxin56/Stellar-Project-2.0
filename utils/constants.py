# Texture paths

texture_earth = 'textures/8k_earth_daymap.jpg'
texture_sun = 'textures/8k_sun.jpg'
texture_background = 'textures/8k_stars_milky_way.jpg'
texture_mercury = 'textures/8k_mercury.jpg'
texture_moon = 'textures/8k_moon.jpg'
texture_mars = 'textures/8k_mercury.jpg'


# Constants related to physics
GRAVITY_CONSTANT = 6.67408/pow(10,11)    # Gravity constant
STD_GRAVITY_PARAMETER = GRAVITY_CONSTANT*(1.989*(pow(10,30)))
TIME_SCALE = 1.0

# Values needed for calculations
SUN_MASS = 1.989*(pow(10,30))      # Sun mass
SUN_RADIUS = 2

EARTH_MASS = 5.972*pow(10,24)
EARTH_SMA = 149.6*pow(10,9)
EARTH_RADIUS = 1
EARTH_ECCENTRICITY = 0.017

MOON_ECCENTRICITY = 0.0549
MOON_MASS = 7.346*pow(10,22)
MOON_SMA = 3.84399*pow(10,5)
MOON_RADIUS = 0.6

MERCURY_ECCENTRICITY = 0.2056
MERCURY_MASS = 3.3011 * pow(10, 23)  # kg
MERCURY_SMA = 5.7909227 * pow(10, 7)  # km
MERCURY_RADIUS = 0.383  # Earth radius

VENUS_ECCENTRICITY = 0.0067
VENUS_MASS = 4.8675 * pow(10, 24)  # kg
VENUS_SMA = 1.08209475 * pow(10, 8)  # km
VENUS_RADIUS = 0.949  # Earth radii

MARS_ECCENTRICITY = 0.0934
MARS_MASS = 6.4171 * pow(10, 23)  # kg
MARS_SMA = 2.2794382 * pow(10, 8)  # km
MARS_RADIUS = 0.532  # Earth radii