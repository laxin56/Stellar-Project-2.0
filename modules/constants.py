
#Global variables which are constants needed for calculations

SIMULATION_TIME = 0
SUN_MASS = 1.989*(pow(10,30))      # Sun mass
GRAVITY_CONSTANT = 6.67408/pow(10,11)    # Gravity constant
STD_GRAVITY_PARAMETER = GRAVITY_CONSTANT*SUN_MASS
EARTH_MASS = 5.972*pow(10,24)
EARTH_SMA = 149.6*pow(10,9)
EARTH_RADIUS = 6378*pow(10,3)


Coll_Mass = {
    'Mercury': 0.06*EARTH_MASS,
    'Venus': 0.81*EARTH_MASS,
    'Earth': EARTH_MASS,
    'Mars': 0.11*EARTH_MASS,
    'Jupiter': 317.83*EARTH_MASS,
    'Saturn': 95.16*EARTH_MASS,
    'Uranus': 14.54*EARTH_MASS,
    'Neptune': 17.15*EARTH_MASS
}

Coll_SMA = {
    'Mercury': 0.39*EARTH_SMA,
    'Venus': 0.72*EARTH_SMA,
    'Earth': EARTH_SMA,
    'Mars': 1.52*EARTH_SMA,
    'Jupiter': 5.20*EARTH_SMA,
    'Saturn': 9.54*EARTH_SMA,
    'Uranus': 19.19*EARTH_SMA,
    'Neptune': 30.07*EARTH_SMA
}

Coll_Eccentricity = {
    'Mercury': 0.206,
    'Venus': 0.007,
    'Earth': 0.017,
    'Mars': 0.093,
    'Jupiter': 0.048,
    'Saturn': 0.054,
    'Uranus': 0.047,
    'Neptune': 0.009
}

Coll_Radius = {
    'Mercury': 0.383,
    'Venus': 0.949,
    'Earth': 1.0,
    'Mars': 0.532,
    'Jupiter': 11.209,
    'Saturn': 9.449,
    'Uranus': 4.007,
    'Neptune': 3.883
}




