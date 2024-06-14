
import pygame
import time
from grav_potential import Vg

pygame.init()
clock = pygame.time.Clock()

# Physics
# Mass of the object in the center (COG)
M = 5.972e24

# Colours
yellow = (255, 174, 66)

size = width, height = (800, 800)
# Screen
screen = pygame.display.set_mode(size)

# Font
mediumFont = pygame.font.Font("fonts/OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("fonts/OpenSans-Regular.ttf", 40)

mediumFont.bold = True

# Running switch
running = True
# Other switches
pointA, pointB = None, None
circleA, circleB = None, None
d1, d2 = None, None
to_refresh = False


def distance(coord1, coord2):
    """Returns the distance between the two coordinates"""
    return ((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)**0.5

grav_body_pos = screen.get_width()/2, screen.get_height()/2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONUP and not to_refresh:
            if not pointA:
                pointA = pygame.mouse.get_pos()
                circleA = round(distance(grav_body_pos, pointA))
            elif not pointB:
                pointB = pygame.mouse.get_pos()
                circleB = round(distance(grav_body_pos, pointB))
        elif to_refresh:
            to_refresh = False
                
    
    screen.fill("black")
    
    pygame.draw.circle(
        screen,
        yellow,
        grav_body_pos,
        20)
    if not (pointA and pointB):
        point = "B" if pointA else "A"
        top_msg_surface = mediumFont.render(f"Select Point {point}", True, "white")
        mouse_pos = pygame.mouse.get_pos()
        r = distance(grav_body_pos, mouse_pos)*1000
        bottom_msg_surface = mediumFont.render(
            f"Gravitational Potential at distance {round(r, 2)} is {Vg(r, M)}",
            True,
            "white"
            )
    elif not pointB:
        # PointB is None
        top_msg_surface = mediumFont.render("Select Point B", True, "white")
    else:
        top_msg_surface = mediumFont.render("Gravitational Potential Difference Shown", True, "white")
        refresh_button = pygame.Rect(width-100, 10, 100, 20)
        refresh_msg = mediumFont.render("Refresh", True, "black")
        refreshRect = refresh_msg.get_rect()
        refreshRect.center = refresh_button.center
        pygame.draw.rect(screen, "white", refresh_button)
        screen.blit(refresh_msg, refreshRect)
        to_refresh = True
        diff = d2 - d1
        bottom_msg_surface = mediumFont.render(
            f"Gravitational Potential Difference between A and B is {round(r, 2)} is {Vg(r, M)}",
            True,
            "white"
            )

    if pointB:
        pygame.draw.circle(
                    screen,
                    "gold",
                    grav_body_pos,
                    circleB,
                    1
                )
        pygame.draw.circle(screen, "orange", pointB, 3)
        point_captionB = mediumFont.render("B", True, "red")
        caption_rectB = point_captionB.get_rect()
        caption_rectB.center = pointB
        screen.blit(point_captionB, caption_rectB)
    if pointA:
        # print(circleA)
        pygame.draw.circle(
                    screen,
                    "gold",
                    grav_body_pos,
                    circleA,
                    1
                )
        pygame.draw.circle(screen, "orange", pointA, 3)
        point_captionA = mediumFont.render("A", True, "red")
        caption_rectA = point_captionA.get_rect()
        caption_rectA.center = pointA
        screen.blit(point_captionA, caption_rectA)

    screen.blit(top_msg_surface, (0, 0))
    pygame.draw.line(screen, "gray", (0, 30), (800, 30), 1)

    screen.blit(bottom_msg_surface, (0, screen.get_height()-32))
    pygame.draw.line(screen, "gray", (0, screen.get_height()-31), (800, screen.get_height()-31))

    # Check if button is clicked
    click, _, _ = pygame.mouse.get_pressed()
    if click == 1 and to_refresh:
        mouse = pygame.mouse.get_pos()
        if refresh_button.collidepoint(mouse):
            time.sleep(0.2)
            circleA, circleB, pointA, pointB = None, None, None, None

    pygame.display.flip()
    clock.tick(24)

pygame.quit()
    

