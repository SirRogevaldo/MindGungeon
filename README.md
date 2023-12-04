# MindGungeon

MindGungeon is a game where you shoot your way through the Gungeon: a mysterious dungeon of gun related enemies, get upgrades and better your weapon skills to defeat the Boss and become The Mind of The Gungeon.

"Can you prove yourself and be the biggest mind of the Gungeon?" - Some old man
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
******

## File Organization

- **main.py** contains the file that runs the game on compiling
- **actor.py** houses the actor class used by objects that are controllable by player (in this case inherited by player.py only)
- **all_bullets.py** **singleton** class used to manage all current bullets in the screen
- **all_enemies.py** **singleton** class used to manage all current enemies in the screen
- **audio_manager.py** file containing all the initialization of sounds and their functions
- **bullet.py** class containing all the logic of the bullet object and created bullet types
- **collision_detector.py** file containing all the functions responsible for collision detection and handling
- **commands.py** file responsible for implementing the **command** pattern, used to process player's inputs to control the character
- **cursor.py** file containing the function to draw the cursor depending on gun type currently held
- **enemies.py** file containing all the logic behind enemies, responsible for implementing the **prototype** pattern for spawning the enemies.
- **enemySprites.py** file containing the class responsible for drawing the enemy sprites, inherits the SpriteSheet class from sprites.py
- **map_load.py** file containing the Tile class and the functions responsible for reading the level maps contained in the map.json file in **Bytecode**
- **player.py** file containing the Gunman class, responsible for all the logic about the player character
- **playerSprite.py** file containing the class responsible for drawing the player sprite, inherits the SpriteSheet class from sprites.py
- **powerups.py** file containing the logic behind obtaining powerups and updating the player accordingly
- **sprites.py** file containing the SpriteSheet class, used to facilitate the image use for the sprites.
- **stats_ui** class used to display the current health and other information about the player's stats on screen
- **subject** class that implements the **Observer** pattern used by the player and enemies, mainly for damage taking and the player's bullet wipe ability


- **test** contains tests to certain source modules

- **src** contains the implemented source code

## Compiling The Game
```
python3 main.py
```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

******
