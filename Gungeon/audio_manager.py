import os
import pygame

pygame.mixer.init()
# Music
pygame.mixer.music.load(os.path.join('Assets', 'Sounds', '1-TheHollowHowl.mp3'))
pygame.mixer.music.set_volume(0.1)

def music_play():
    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=2000)

# Sound Effects
Shotgun_sound = pygame.mixer.Sound(os.path.join('Assets', 'Sounds', 'ShotgunShot.mp3'))
Shotgun_sound.set_volume(0.1)

def Shotgun_play(entity):
    Shotgun_sound.play()

enemy_hit_sound = pygame.mixer.Sound(os.path.join('Assets', 'Sounds', 'EnemyHit.mp3'))
enemy_hit_sound.set_volume(0.2)

def Enemy_hit_play(entity):
    enemy_hit_sound.play()

player_wipe_sound = pygame.mixer.Sound(os.path.join('Assets', 'Sounds', 'Wipe.mp3'))
player_wipe_sound.set_volume(0.5)

def Player_wipe_play(entity):
    player_wipe_sound.play()

player_shot_sound = pygame.mixer.Sound(os.path.join('Assets', 'Sounds', 'PlayerShot.mp3'))
player_shot_sound.set_volume(0.1)

def Player_shot_play(entity):
    player_shot_sound.play()