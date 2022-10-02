from sys import path

path.insert(0, "./src/ty_command")

import ty  # type: ignore

with open("README.md", "w") as f:
    f.write(ty.__doc__)
