from .models import File


def nwp_file_list(body, **kwargs):
    files = []
    for line in body.split("=\n"):
        if not line:
            continue
        try:
            filename, _ = line.replace(" ", "").split(",")[:2]
            files += [File(filename=filename)]
        except Exception as ex:
            raise ex
    return files


def download_nwp_file(body, **kwargs):
    if not isinstance(body, dict) or not body.get("filename"):
        raise KeyError(body)
    return File(
        filename=body["filename"],
        content=body["content"],
    )


def sat(body, **kwargs):
    if not isinstance(body, dict) or not body.get("filename"):
        raise KeyError(body)
    return File(
        filename=body["filename"],
        content=body["content"],
    )


def sat_ana_txt(body, **kwargs):
    records = []
    for line in body.split("\n"):
        if line.startswith("#"):
            print(line)
            continue
        if not line:
            continue
        records += [x.strip() for x in line.split(",")][:-1]
    return records


def rdr(body, **kwargs):
    if not isinstance(body, dict) or not body.get("filename"):
        raise KeyError(body)
    return File(
        filename=body["filename"],
        content=body["content"],
    )
