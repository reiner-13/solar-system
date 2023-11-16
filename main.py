import pygame
import sys
from pygame.locals import *
import planet

pygame.init()
pygame.font.init()
pygame.display.set_caption("Solar System")

WINDOW_SIZE = (1600, 900)
CENTER = (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 200)
YELLOW = (200, 200, 0)
RED = (200, 0, 0)
GRAY = (150, 150, 150)
ORANGE = (200, 100, 0)
BEIGE = (225, 200, 150)


# VISUAL TRICKERY
SUN_RAD_SCALING_VALUE = 1 # sun's radius (km) get scaled down by this amount visually
PLANET_RAD_SCALING_VALUE = 1 # planets' radii (km) get scaled down by this amount visually


img_path = "./images"
program_icon = pygame.image.load(f"{img_path}/sun.webp")
pygame.display.set_icon(program_icon)

planet_info = {
    # RADIUS (equatorial) UNITS - km
    # MASS UNITS - 10^24 kg
    # DIST TO SUN UNITS - km
    "Sun": {
        "radius": 695700, "mass": 0, "dist": 0, "color": YELLOW
    },
    "Mercury": {
        "radius": 2440.5, "mass": 0.3301, "dist": 57909000, "color": GRAY
    },
    "Venus": {
        "radius": 6051.8, "mass": 4.8673, "dist": 108210000, "color": ORANGE
    },
    "Earth": {
        "radius": 6378.137, "mass": 5.9722, "dist": 149598000, "color": BLUE
    },
    "Mars": {
        "radius": 3396.2, "mass": 0.64169, "dist": 227956000, "color": RED
    },
    "Jupiter": {
        "radius": 71492, "mass": 1898.13, "dist": 778479000, "color": ORANGE
    },
    "Saturn": {
        "radius": 60268, "mass": 568.32, "dist": 1432041000, "color": BEIGE
    }
}
planets = []
for p in planet_info.keys():
    if p == "Sun":
        sun = planet.Planet(p, planet_info[p]["radius"], planet_info[p]["mass"], planet_info[p]["dist"], planet_info[p]["color"])
        continue
    planets.append(planet.Planet(p, planet_info[p]["radius"], planet_info[p]["mass"], planet_info[p]["dist"], planet_info[p]["color"]))
for p in planets:
    p.print()

time = 0
zoom = 1000
running = True
while running: # MAIN LOOP

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                zoom = max(1, zoom - 100)
            if event.button == 5:
                zoom = min(zoom + 100, 100000)
    print(zoom)
    print(planets[1].time)
    screen.fill(BLACK)
    
    pygame.draw.circle(screen, sun.color, sun.position, sun.radius / (SUN_RAD_SCALING_VALUE * zoom))
    for p in planets:
        p.orbit(zoom)
        pygame.draw.circle(screen, p.color, p.position, p.radius / (PLANET_RAD_SCALING_VALUE * zoom))
        
    pygame.display.flip()



pygame.quit()

