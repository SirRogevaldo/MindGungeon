class Actor:
    def update(self):
        raise NotImplementedError("Subclasses must implement this method")
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    def wipe(self):
        raise NotImplementedError("Subclasses must implement this method")