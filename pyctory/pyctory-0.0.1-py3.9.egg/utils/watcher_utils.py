"""
Most of the entity's information can be derived in real time from the Entity object
Only information that is not relevant to the entity's real-time simulation is recorded here
"""


class EntityState:
    STATE_IDLE = 0
    STATE_BUSY = 1

    def __init__(self) -> None:
        """ belows are for Processor """
        self.used_time = 0
        self.free_time = 0
        self.prev_state = EntityState.STATE_IDLE
        self.prev_time = 0
        self.curr_state = EntityState.STATE_IDLE
