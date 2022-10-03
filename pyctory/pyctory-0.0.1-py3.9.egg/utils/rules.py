from typing import Tuple
import random

from ..classes.base import BasicClass
from ..classes.source import Source
from ..classes.buffer import Buffer
from ..classes.processor import Processor
from ..classes.scene import Scene


def fifo(sc: Scene, eName: str, t: int) -> Tuple[str, str]:
    e: BasicClass = sc.entities[eName]
    if e in sc.sources:
        assert type(e) is Source
        return (list(sc.graph[eName].keys())[0],
                list(e.items_ready.keys())[0])
    elif e in sc.buffers:
        assert type(e) is Buffer
        down_e = e.pipe1[e.p1s[0]][0]
        return down_e.name, e.itemHeap[0][1].name
    elif e in sc.processors:
        assert type(e) is Processor
        return (list(sc.graph[eName].keys())[0],
                list(e.items_ready.keys())[0])
    elif e in sc.sinks:
        raise RuntimeError(f'Sink {e.name} outputs')
    raise RuntimeError(f'invalid entity<{eName}>')


def lifo(sc: Scene, eName: str, t: int) -> Tuple[str, str]:
    e: BasicClass = sc.entities[eName]
    if e in sc.sources:
        assert type(e) is Source
        return (list(sc.graph[eName].keys())[0],
                list(e.items_ready.keys())[0])
    elif e in sc.buffers:
        assert type(e) is Buffer
        down_e = e.pipe1[e.p1s[0]][0]
        return down_e.name, e.itemHeap[-1][1].name
    elif e in sc.processors:
        assert type(e) is Processor
        return (list(sc.graph[eName].keys())[0],
                list(e.items_ready.keys())[0])
    elif e in sc.sinks:
        raise RuntimeError(f'Sink {e.name} outputs')
    raise RuntimeError(f'invalid entity<{eName}>')


def randio(sc: Scene, eName: str, t: int) -> Tuple[str, str]:
    e: BasicClass = sc.entities[eName]
    if e in sc.sources:
        assert type(e) is Source
        return (list(sc.graph[eName].keys())[0],
                list(e.items_ready.keys())[0])
    elif e in sc.buffers:
        assert type(e) is Buffer
        down_e = e.pipe1[e.p1s[0]][0]
        i = int(random.random() * len(e.itemHeap) // 1)
        return down_e.name, e.itemHeap[i][1].name
    elif e in sc.processors:
        assert type(e) is Processor
        return (list(sc.graph[eName].keys())[0],
                list(e.items_ready.keys())[0])
    elif e in sc.sinks:
        raise RuntimeError(f'Sink {e.name} outputs')
    raise RuntimeError(f'invalid entity<{eName}>')
