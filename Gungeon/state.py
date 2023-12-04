class State:
    def __init__(self,name) -> None:
        self.name = name

    def enter(self):
        print(f"Entering state: {self.name}")
    
    def update(self,object):
        pass

    def exit(self):
        print(f"Exiting state: {self.name}")

class Transition:

    def __init__(self, _from, _to) -> None:
        self._from = _from
        self._to = _to

class Default(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, object):
        print("Default Animation")
        return super().update(object)
    
class Invincible(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, object):
        print("Invincible Animation")
        return super().update(object)

class Death(State):
    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, object):
        print("DEATH Animation")
        return super().update(object)