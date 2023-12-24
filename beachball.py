import pygame as pg
from pygame.math import Vector2
import math

class BeachBall(pg.sprite.Sprite):
     
    def __init__(self, waypoints, image):
        pg.sprite.Sprite.__init__(self)
        
        self.waypoints = waypoints
        self.pos = Vector2(waypoints[0])
        self.next_index = 1 # starts at index 0, next waypoint is index 1
        
        self.velocity = 2
        
        self.angle = 0
        self.original_image = image
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
    
    def update(self):
        self.move()
        self.rotate()
        
    def move(self):
        # check if there are any remaining waypoints
        if(self.next_index < len(self.waypoints)):
            # determine next waypoint and distance to next waypoint
            self.next_waypoint = Vector2(self.waypoints[self.next_index])
            self.movement = self.next_waypoint - self.pos
        else:
            # beachball has passed through all waypoints
            self.kill()
        
        # if the distance is greater than the speed, move normally
        # else slow down
        distance = self.movement.length()
        if(distance >= self.velocity):
            # normalize x and y distances and add each to the enemy's respective x and y coordinates
            self.pos += self.movement.normalize() * self.velocity
        else:
            # check if the distance is 0 b/c cannot multiply by distance vector
            if(distance != 0):
                self.pos += self.movement.normalize() * distance
            
            # start moving to next waypoint
            self.next_index += 1
            
        # update center of rect
        #self.rect.center = self.pos   <-- no longer needed since updated in rotate() which is called right after
        
    def rotate(self):
        distance = self.next_waypoint - self.pos
        # use the x and y distances to the next waypoint to calculate the angle to rotate the sprite at
        self.angle = math.degrees(math.atan2(-distance[1], distance[0]))  # arctan of -y/x
        
        # update image the center of the rect
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos