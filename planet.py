import pygame
import math

WINDOW_SIZE = (1600, 900)
CENTER = (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)
DIST_TO_SUN_SCALING_VALUE = 150 #2500000

G_CONST = 0.00000000066743 # 6.6743 * 10^-11 m^3 / (kg * s^2)
SUN_MASS = 1_988_500 * 10**24
GM = 132712 * 10**6

class Planet:

    def __init__(self, name, radius, mass, dist, color):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.dist = dist
        self.color = color
        self.velocity = 0 # KM / S
        self.position = [(CENTER[0] + (dist / (DIST_TO_SUN_SCALING_VALUE * 20))), CENTER[1]]
        self.time = 0

    def print(self):
        print(f"Name:\t{self.name}")
        print(f"Radius:\t{self.radius} km")
        print(f"Mass:\t{self.mass} * 10^24 kg")
        print(f"Position:\t{self.position}")
        print(self.velocity)
        print()

    def orbit(self, zoom):
        self.time += 0.0001
        self.velocity = math.sqrt(GM / (self.dist)) # GM would need to be something else if I were to implement moons

        if self.time * self.velocity >= 2 * math.pi: # resets time after a rotation
            self.time = 0
        self.position[0] = CENTER[0] + (self.dist / (DIST_TO_SUN_SCALING_VALUE * zoom)) * math.cos(self.time * self.velocity)
        self.position[1] = CENTER[1] + (self.dist / (DIST_TO_SUN_SCALING_VALUE * zoom)) * math.sin(self.time * self.velocity)
        