from .stub import f, stub

if __name__ == "__main__":
    with stub.run():
        for x in f.map([1, 2, 3]):
            pass
