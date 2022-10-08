from __future__ import annotations

from typing import Any

from yaml import safe_dump, safe_load


def sort_key(data: tuple[str, dict[str, Any]]):
    key, value = data
    return (value["stat"], 1 if "heal" in value else 0, value["multiplier"], key)


def sort_yaml_and_save(path):
    with open(path, encoding="utf-8") as f:
        data = safe_load(f)
    data = dict(sorted(data.items(), key=sort_key))
    with open(path, "w", encoding="utf-8") as f:
        safe_dump(data, f, allow_unicode=True, sort_keys=False)


if __name__ == "__main__":
    from pathlib import Path

    for yml_file in Path("julgi/skill").rglob("*.yml"):
        print(f"Process {yml_file}...")
        sort_yaml_and_save(yml_file)
