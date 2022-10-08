from trainerbase.gameobject import GameObject

import objects


class Teleport:
    def __init__(
        self,
        player_x: GameObject,
        player_y: GameObject,
        player_z: GameObject,
        labels: dict[str, tuple[int]] = None,
    ):
        self.player_x = player_x
        self.player_y = player_y
        self.player_z = player_z
        self.labels = {} if labels is None else labels

    def set_coords(self, x: float, y: float, z: float = 100):
        self.player_x.value = x
        self.player_y.value = y
        self.player_z.value = z

    def get_coords(self):
        return self.player_x.value, self.player_y.value, self.player_z.value

    def goto(self, label: str):
        self.set_coords(*self.labels[label])
