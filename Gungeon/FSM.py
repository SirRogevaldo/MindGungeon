from state import State, Default, Invincible, Death, Transition

class FSM:
    def __init__(self, states: list[State], transitions: dict[Transition]) -> None:
        self._states = states
        self._transitions = transitions

        self.current: State = self._states[0]
        self.end: State = self._states[-1]

    def update(self, event, object):
        if event:
            trans = self._transitions.get(event)
            if trans and trans._from == self.current:
                self.current.exit()
                self.current = trans._to
                self.current.enter()
            self.current.update(object)
            
            if self.current == self.end:
                self.current.exit()
                return False
            return True
        
if __name__ == "__main__":
    default = Default()
    invincible = Invincible()
    death = Death()

    states = [default, invincible, death]
    transitions = {
        "damaged":   Transition(default, invincible),
        "composed": Transition(invincible, default),
        "dead":   Transition(default, death)
    }
    
    fsm = FSM(states, transitions)

    event = None
    while fsm.update(event, None):
        event = input(">")