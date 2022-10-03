import time
from typing import Callable, List, Tuple

from ovtable import OvTable

from pyctory.classes import Scene, BasicClass, Item


def get_ovtable_render_function(scene: Scene, _str: bool = False) -> Tuple[Callable, OvTable]:
    ot = OvTable(width=150, height=38, print_to_terminal=_str)
    ot.add_row(1)
    for lev in scene.levels:
        ot.add_row(len(lev))

    def ovtable_render_function():
        ot[0, 0] = (f'Scene: {scene.name} current time: {scene.time}', 'w')

        for x, l in enumerate(scene.levels):
            x = x + 1
            for y, eName in enumerate(l):
                e: BasicClass = scene.entities[eName]
                ot[x, y] = [(f'{e.className}', 'c'), (f'<{e.name}>', 'y'), (' ', 'b')]
                """ add items """
                ot[x, y] += [('[', 'w')]
                if e.max_size <= scene.config.render_in_terminal_max_pos:
                    """ if postions is limited """
                    for i in range(e.max_size):
                        if i != 0:
                            ot[x, y] += [(', ', 'w')]
                        if i in e.pos_items.keys():
                            ot[x, y] += [(f'{e.pos_items[i].name}', 'r')]
                        else:
                            ot[x, y] += [('___', 'w')]
                else:
                    """ if postions is unlimited, prioritize the first few items of the itemHeap """
                    items: List[Item] = e.items
                    if e.className == 'Buffer':
                        items = [t[1] for t in e.itemHeap]
                    if e.className == 'Source':
                        items = list(e.items_ready.values())
                    for i, t in enumerate(items):
                        if i != 0:
                            ot[x, y] += [(', ', 'w')]
                        if i >= scene.config.render_in_terminal_max_pos:
                            ot[x, y] += [(f'...{len(items) - i} more', 'r')]
                            break
                        ot[x, y] += [(f'{t.name}', 'r')]
                ot[x, y] += [(']', 'w')]

        if not _str:
            ot.render()
            time.sleep(scene.config.render_in_terminal_interval)

    return ovtable_render_function, ot
