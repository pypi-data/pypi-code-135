import json
from io import StringIO

from gantry.logger.utils import _build_batch_iterator


def test_build_batch_iterator():
    event_list = [{1: 1}, {2: 2}, {3: 3}, {4: 4}, {5: 5}]
    # We should only have 3 batches created from the list.
    batch_iter = _build_batch_iterator(event_list, 2)
    iters = 0
    for _ in batch_iter:
        iters += 1
    assert iters == 3

    # We should still have all 5 lines in the file
    batch_iter = _build_batch_iterator(event_list, 2)
    result = "".join([part.decode("utf-8") for part in batch_iter])
    file = StringIO(result)

    for line in file.readlines():
        json.loads(line)

    file.seek(0)
    assert len(file.readlines()) == 5
