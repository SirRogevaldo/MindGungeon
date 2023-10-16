class Actor:
    def update(self):
        raise NotImplementedError("Subclasses must implement this method")

    def get_left_pressed(self):
        raise NotImplemented

    def get_right_pressed(self):
        raise NotImplemented

    def get_up_pressed(self):
        raise NotImplemented

    def get_down_pressed(self):
        raise NotImplemented
    
    def set_left_pressed(self, pressed):
        raise NotImplemented
    
    def set_right_pressed(self, pressed):
        raise NotImplemented
    
    def set_up_pressed(self, pressed):
        raise NotImplemented
    
    def set_down_pressed(self, pressed):
        raise NotImplemented