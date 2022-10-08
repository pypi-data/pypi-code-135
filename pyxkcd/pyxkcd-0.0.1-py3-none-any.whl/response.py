import datetime

class Response:
    def __init__(self, response):
        self._response = response
        self.released = datetime.datetime(int(response["year"]), int(response["month"]), int(response["day"]))
        self.link = response["link"]
        self.title = response["title"]
        self.alt = response["alt"]
        self.num = response["num"]
        self.img = response["img"]
        self.transcript = response["transcript"]

    def json(self):
        return self._response

    def raw(self):
        return self._response

    def __eq__(self, __o):
        return self.json() == __o.json()

    def __dict__(self):
        return self._response

    def __str__(self):
        return f"{self.num}: {self.title}"

    def __repr__(self):
        return f"<Response({self._response})>"