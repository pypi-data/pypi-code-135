import typing


class OverloadList(list):
    """A list subclass.

    """


class OverloadDict(dict[typing.Any, OverloadList]):
    """Similar to a dictionary, but turns multiple occurances of a key into a list of
    values intead of overwriting the previous value.

    Additionally, multiple keys and values can be set at once, for example:
    ```
    d = OverloadDict()
    d["a", "b", "c"] = 1, 2, 3
    ```

    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    def __setitem__(self, __k, __v) -> None:
        if type(__k) == tuple and type(__v) not in [tuple, list]:
            return print(f"multiple values must be used if assigning multiple keys. Expected {len(__k)}, got 1.")
        if type(__k) == tuple:
            for k, v in zip(__k, __v):
                self[k].append(v) if __k in self else super().__setitem__(k, OverloadList([v]))
            return
        return self[__k].append(__v) if __k in self else super().__setitem__(__k, OverloadList([__v]))
