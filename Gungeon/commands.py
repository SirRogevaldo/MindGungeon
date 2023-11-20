import pygame
from actor import Actor

class Command:
    def pressed(self, actor: Actor):
        raise NotImplementedError("Subclasses must implement this method")
    
class Up(Command):
    def pressed(self,actor: Actor):
        actor.move(0,-1)

class Down(Command):
    def pressed(self,actor: Actor):
        actor.move(0,1)
    
class Left(Command):
    def pressed(self,actor: Actor):
        actor.move(-1,0)

class Right(Command):
    def pressed(self,actor: Actor):
        actor.move(1,0)

class Wipe(Command):
    def pressed(self,actor: Actor):
        actor.wipe()


class InputHandler:
    command = {
        pygame.K_w: Up(),
        pygame.K_s: Down(),
        pygame.K_a: Left(),
        pygame.K_d: Right(),
        pygame.K_q: Wipe(),
    }

    def handleInput(self,keys):

        wasd = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_q]

        commands = []

        for key in wasd:
            if keys[key]:
                commands.append(self.command[key])

        return commands
 

