import pygame as pg
import sys
import constants as c
from beachball import BeachBall

def main():
    # initalize pygame
    pg.init()
    
    # intialize clock
    clock = pg.time.Clock()
    
    
    # Create the game window
    screen_width = pg.display.Info().current_w
    screen_height = pg.display.Info().current_h
    
    screen = pg.display.set_mode((screen_width, screen_height - c.TASKBAR_HEIGHT))
    pg.display.set_caption("OctoOdyssey")
    
    # load images
    beachball_image = pg.image.load('assets/beachball.png').convert_alpha()
    beachball_image = pg.transform.scale(beachball_image, (64, 64))

    
    
    # create sprite group for enemies
    enemy_group = pg.sprite.Group()
    waypoints = [(100, 200), (300, 400), (50, 600)]
    beachball = BeachBall(waypoints, beachball_image)
    enemy_group.add(beachball)
    
    # game loop
    run = True
    while run:
        clock.tick(c.FPS)
        
        # refresh background
        screen.fill('gray100')
        
        # update groups
        for enemy in enemy_group:
            enemy.update()
            
        # draw groups
        enemy_group.draw(screen)
        
        # event handling
        for event in pg.event.get():
            
            
            # quitting the game
            if event.type == pg.QUIT:
                run = False
                
        
        # update display
        pg.display.flip()

    
    # quit the game and end the program
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()
