from typing import Tuple, Any


def connect(
    e1: Any, e2: Any,
    p1: int = -1, p0: int = -1,
    strict: bool = True
) -> Tuple[int, int]:

    assert p1 >= -1, f'{p1} not a valid port number'
    assert p0 >= -1, f'{p0} not a valid port number'

    if strict:
        assert p1 not in e1.pipe1.keys(), \
            f'output port {p1} of {e1.name} is already occupied'
        assert p0 not in e2.pipe0.keys(), \
            f'output port {p0} of {e2.name} is already occupied'

    if p1 == -1:
        _p1 = 0
        while _p1 in e1.pipe1.keys():
            _p1 += 1
        p1 = _p1
    if p0 == -1:
        _p0 = 0
        while _p0 in e2.pipe0.keys():
            _p0 += 1
        p0 = _p0

    e1.pipe1[p1] = (e2, p0)
    e2.pipe0[p0] = (e1, p1)

    return (p1, p0)


def disconnect(
    e1: Any, e2: Any,
    strict: bool = True
) -> int:
    connectTuples: Tuple[int, int] = []
    p1_list = list(e1.pipe1.keys())
    p0_list = list(e2.pipe0.keys())

    for p1 in p1_list:
        for p0 in p0_list:
            if e1.pipe1[p1] == (e2, p0) and \
                    e2.pipe0[p0] == (e1, p1):
                connectTuples.append((p1, p0))

    if strict:
        assert len(connectTuples) != 0, \
            f'no connection between {e1.name} and {e2.name}'

    for (p1, p0) in connectTuples:
        del e1.pipe1[p1]
        del e2.pipe0[p0]

    return len(connectTuples)
