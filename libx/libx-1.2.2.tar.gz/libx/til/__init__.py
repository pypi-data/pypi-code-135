"""
Utils that provide a List of map & composite paths.
Useful to make logic in scpts and dependent libs more readable.
"""

from pathlib import Path

# map a list to a func and get the resulting list.
lmap = lambda f, l: list(map(f, l))
# Compose paths from strs.
glue = lambda *argp: Path.cwd().joinpath(*lmap(istr, argp))
# Run f n times and put results in a list.
spawn = lambda f, n, *args: [f(*args) for _ in range(n)]
