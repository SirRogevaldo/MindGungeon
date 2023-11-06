import pygame
from actor import Actor

class Command:
    def pressed(self,value, actor: Actor):
        raise NotImplementedError("Subclasses must implement this method")
    
class Up(Command):
    def pressed(self,value,actor: Actor):
        actor.set_up_pressed(value)
        if value:
            actor.move(0,-1)

class Down(Command):
    def pressed(self,value,actor: Actor):
        actor.set_down_pressed(value)
        if value:
            actor.move(0,1)
    
class Left(Command):
    def pressed(self,value,actor: Actor):
        actor.set_left_pressed(value)
        if value:
            actor.move(-1,0)

class Right(Command):
    def pressed(self,value,actor: Actor):
        actor.set_right_pressed(value)
        if value:
            actor.move(1,0)

class Mouse_move(Command):
    def move(self, value, actor: Actor):
        actor.set_mouse_pos(value)

class InputHandler:
    command = {
        pygame.K_w: Up(),
        pygame.K_s: Down(),
        pygame.K_a: Left(),
        pygame.K_d: Right(),
        pygame.MOUSEMOTION: Mouse_move()
    }

    def handleInput(self,keys, actor: Actor):

        wasd = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]

        for key in wasd:
            self.command[key].pressed(keys[key],actor)

    
    def handleMouse(self, mouse, actor: Actor):
        self.command[pygame.MOUSEMOTION].move(mouse,actor)
