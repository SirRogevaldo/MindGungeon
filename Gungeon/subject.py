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