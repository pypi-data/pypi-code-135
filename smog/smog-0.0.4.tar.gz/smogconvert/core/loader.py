import json


def specloader(fnam):
    lines = []
    with open(fnam) as f:
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            pos = line.find("#")
            if pos >= 0:
                line = line[:pos]
            if len(line.strip()) == 0:
                continue
            lines.append(line.rstrip())

    cont = "\n".join(lines)
    procs = json.loads(cont)

    return procs
