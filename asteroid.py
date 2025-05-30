import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # split_angle_1 = random.uniform(0, 359)
            # split_angle_2 = random.uniform(0, 359)
            # angle_1 = self.velocity.rotate(split_angle_1)
            # angle_2 = self.velocity.rotate(split_angle_2)
            # new_radius = self.radius - ASTEROID_MIN_RADIUS
            # asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            # asteroid.velocity = angle_1 * 1.2
            # asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            # asteroid.velocity = angle_2 * 1.2

            num_to_spawn = random.randint(1, 40)
            for i in range(2, num_to_spawn + 1):
                new_radius = self.radius - ASTEROID_MIN_RADIUS
                asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                asteroid.velocity = self.velocity.rotate(random.uniform(0,359)) * 1.2
                