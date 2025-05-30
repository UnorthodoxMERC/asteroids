import pygame
from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y, radius, shots_group):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.shots_group = shots_group
        self.timer = 0
        

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if self.timer < 0:
            self.timer = 0
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            direction = pygame.Vector2(0, 1)
            direction = direction.rotate(self.rotation)
            new_shot.velocity = direction * PLAYER_SHOOT_SPEED
            self.shots_group.add(new_shot)
            self.timer = PLAYER_SHOOT_COOLDOWN
        

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
            
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius) 

    def update(self, dt):
        self.position += (self.velocity * dt)