import pygame

def drawCursor(type, display):
    x, y = pygame.mouse.get_pos()

    # Default
    color_outer  = (255, 0, 0)
    color_middle = (  0, 0, 0)
    color_inner  = (255, 0, 0)

    match type:
        case "normal":
            pass
        case "crossbow":
            color_outer = (165, 42, 42)
            color_inner = (165, 42, 42)
        case "missile":
            color_outer  = (255, 255, 255)  
            color_middle = (255,   0,   0) 
            color_inner  = (255, 255, 255) 
        case "cannon":
            color_outer  = (128, 128, 128) 
            color_middle = (  0,   0,   0) 
            color_inner  = (128, 128, 128)  
        case "golden":
            color_outer = (255, 255, 0) 
            color_inner = (255, 255, 0) 

    # Draw the cursor
    pygame.draw.circle(display, color_outer,  (x, y), 15)
    pygame.draw.circle(display, color_middle, (x, y), 10)
    pygame.draw.circle(display, color_inner,  (x, y),  5)


        