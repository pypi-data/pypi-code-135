from functools import reduce
import json
import random
import math
from typing import Dict, List, Tuple

"""
input:
generate_data(
    number=5,
    process_list=["Eating", "digestion", "excretion"],
    typ_dict={"Vegetable": 50, "meat": 30, "carbohydrates": 20},
    process_dict={
        "Eating": {"Vegetable": (40, 5), "meat": (50, 20), "carbohydrates": (20, 3)},
        "digestion": {"Vegetable": (70, 45), "meat": (200, 50), "carbohydrates": (50, 20)},
        "excretion": {"Vegetable": (5, 2), "meat": (10, 5), "carbohydrates": (5, 3)},
    },
    poisson=0.95,
)

output:
{
    "process_list": [
        "Eating",
        "digestion",
        "excretion"
    ],
    "001": {
        "arrival": 1,
        "typ": "meat",
        "Eating": 66,
        "digestion": 204,
        "excretion": 17
    },
    ...
    ...
    "005": {
        "arrival": 38,
        "typ": "Vegetable",
        "Eating": 53,
        "digestion": 31,
        "excretion": 5
    }
}
"""


def generate_data(number: int,
                  process_list: List[str],
                  typ_dict: Dict[str, int],
                  process_dict: Dict[str, Dict[str, Tuple[int, int]]],
                  poisson: float,
                  filepath: str = None,
                  random_seed: int = None,
                  ) -> dict:
    """
    process_list example: ["proc1", "proc2"]  # means process 'proc2' is the next process for 'proc1'
    typ_dict example:
    {
        "typ1": 30,  # typ1 total volume share 30 / (30 + 70)
        "typ2": 70,  # typ2 total volume share 70 / (30 + 70)
    }
    process_dict example:
    {
        "proc1":
        {
            "typ1": (20, 5),  # processing time of "typ1" on process 'proc1' follows a normal distribution of (20, 5)
            "typ2": (14, 8),  # processing time of "typ2" on process 'proc1' follows a normal distribution of (14, 8)
        }
        "proc2":
        {
            "typ1": (30, 2),  # processing time of "typ1" on process 'proc2' follows a normal distribution of (30, 2)
            "typ2": (10, 8),  # processing time of "typ2" on process 'proc2' follows a normal distribution of (10, 8)
        }
    }
    Poisson: 0.5,  # the probability of item arrival per second
                   # (cargo arrival obeys Poisson distribution)

    return value be like:
    """
    if random_seed is not None:
        random.seed(random_seed)

    assert 0 < poisson <= 1, f"poisson {poisson} not in [0, 1)"
    assert set(process_list) == set(process_dict.keys()), \
        "inconsistent process sequence statement"
    for v in process_dict.values():
        assert set(typ_dict.keys()) == set(v.keys()), \
            "inconsistent type statement"

    tim = 0
    items = {}
    items["process_list"] = process_list

    # Roulette Algorithm to choose typ
    _gcd = reduce(math.gcd, list(typ_dict.values()))
    typ_list = []
    for k, v in typ_dict.items():
        typ_list += [k] * (v // _gcd)

    for i in range(number):
        itemName = f"{i + 1 :0>3d}"
        item = {}
        items[itemName] = item

        while random.random() > poisson:
            tim += 1
        item["arrival"] = tim

        typ = random.choice(typ_list)
        item["typ"] = str(typ)

        for k, v in process_dict.items():
            item[k] = max(
                int(round(random.normalvariate(v[typ][0], v[typ][1]))), 1)

        if filepath is not None:
            with open(filepath, 'w') as f:
                f.write(json.dumps(items, indent=2, ensure_ascii=False))

    return items


def load_data(filepath: str) -> dict:
    with open(filepath, 'r') as f:
        items = json.load(f)
    return items
