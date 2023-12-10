"""
    Collision detector:

    -This file contains all the collision detection functions used in the game.
    -This file is used to detect collisions between entities and walls, bullets and walls, bullets and enemies, and bullets and the player and to handle those collisions.
    
"""


def collision_entity_walls(entity, walls):

    for wall in walls:
        if wall.collides(entity.get_rect()):

            if entity.getVelX() != 0:
                entity.setX(entity.last_x)
            if entity.getVelY() != 0: 
                entity.setY(entity.last_y)

def collision_bullet_walls(bullet,walls):

    for wall in walls:
        if wall.collides(bullet.get_rect()):
            return True
    return False

def collision_bullet_enemies(bullet,enemies):

    for enemy in enemies:
        if bullet.is_friendly() and enemy.get_rect().colliderect(bullet.get_rect()):
            enemy.notify(bullet,"hit")
            return True
    return False

def collision_bullet_player(bullet,player):

    if not bullet.is_friendly() and player.get_rect().colliderect(bullet.get_rect()):
            player.notify(bullet,"hit")
            return True
    return False