"""
    ACTOR:
    -houses the actor class used by objects that are controllable by player (in this case inherited by player.py only)
"""
class Actor:
    def update(self):
        raise NotImplementedError("Subclasses must implement this method")
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    def wipe(self):
        raise NotImplementedError("Subclasses must implement this method")