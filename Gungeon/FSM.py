from state import State, Walk, Idle, Death, Transition

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
    walk = Walk()
    idle = Idle()
    death = Death()

    states = [walk, idle, death]
    transitions = {
        "halt":   Transition(walk, idle),
        "sprint": Transition(idle, walk),
        "wDie":   Transition(walk, death), # preciso 2?
        "sDie":   Transition(idle, death)
    }
    
    fsm = FSM(states, transitions)

    event = None
    while fsm.update(event, None):
        event = input(">")