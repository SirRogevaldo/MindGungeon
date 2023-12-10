"""
    Subject class:
    - class that implements the **Observer** pattern used by the player and enemies, mainly for damage taking and the player's bullet wipe ability

"""


class Subject:
    def __init__(self):
        self.events = dict()

    def register(self,event,event_handler):
        if event not in self.events:
            self.events[event] = []
        self.events[event].append(event_handler)

    def notify(self, entity, event):
        for event_handler in self.events[event]:
            event_handler(entity)