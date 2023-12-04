import pygame

def drawCursor(type, display):
    x, y = pygame.mouse.get_pos()

    # Default cursor design
    color_outer  = (255, 0, 0)
    color_middle = (  0, 0, 0)
    color_inner  = (255, 0, 0)

    # Customize cursor design based on weapon type
    match type:
        case "normal":
            pass  # Use default colors
        case "crossbow":
            color_outer = (165, 42, 42)
            color_inner = (165, 42, 42)
        case "missile":
            color_outer  = (255, 255, 255)  # Blue outer color for missile
            color_middle = (255,   0,   0)  # White middle color for missile
            color_inner  = (255, 255, 255)  # Blue inner color for missile
        case "cannon":
            color_outer  = (128, 128, 128)  # Gray outer color for cannon
            color_middle = (  0,   0,   0)  # Black middle color for cannon
            color_inner  = (128, 128, 128)  # Gray inner color for cannon
        case "golden":
            color_outer = (255, 255, 0)  # Golden color
            color_inner = (255, 255, 0)  # Golden color

    # Draw the cursor
    pygame.draw.circle(display, color_outer,  (x, y), 15)
    pygame.draw.circle(display, color_middle, (x, y), 10)
    pygame.draw.circle(display, color_inner,  (x, y),  5)


        