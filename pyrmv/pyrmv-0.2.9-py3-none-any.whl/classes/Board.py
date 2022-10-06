from datetime import datetime
from pyrmv.methods.journey_detail import journey_detail
from pyrmv.methods.stop_by_id import stop_by_id


class LineArrival():

    def __init__(self, data, access_id: str):
        self.journey = journey_detail(access_id, data["JourneyDetailRef"]["ref"])
        self.status = data["JourneyStatus"]
        # self.messages = []
        self.name = data["name"]
        self.type = data["type"]
        self.stop_name = data["stop"]
        self.stop_id = data["stopid"]
        self.stop_id_ext = data["stopExtId"]
        self.stop = stop_by_id(access_id, self.stop_id)
        self.time = datetime.strptime(data["time"], "%H:%M:%S")
        self.date = datetime.strptime(data["date"], "%Y-%m-%d")
        if ("rtTime" in data) and ("rtDate" in data):
            self.time_real_time = datetime.strptime(data["rtTime"], "%H:%M:%S")
            self.date_real_time = datetime.strptime(data["rtDate"], "%Y-%m-%d")
        self.reachable = data["reachable"]
        self.origin = data["origin"]

    def __str__(self) -> str:
        return f"{self.name} coming from {self.origin} at {self.time.time()} {self.date.date()}"

class LineDeparture():

    def __init__(self, data, access_id: str):
        self.journey = journey_detail(access_id, data["JourneyDetailRef"]["ref"])
        self.status = data["JourneyStatus"]
        # self.messages = []
        self.name = data["name"]
        self.type = data["type"]
        self.stop_name = data["stop"]
        self.stop_id = data["stopid"]
        self.stop_id_ext = data["stopExtId"]
        self.stop = stop_by_id(access_id, self.stop_id)
        self.time = datetime.strptime(data["time"], "%H:%M:%S")
        self.date = datetime.strptime(data["date"], "%Y-%m-%d")
        if ("rtTime" in data) and ("rtDate" in data):
            self.time_real_time = datetime.strptime(data["rtTime"], "%H:%M:%S")
            self.date_real_time = datetime.strptime(data["rtDate"], "%Y-%m-%d")
        self.reachable = data["reachable"]
        self.direction = data["direction"]
        self.direction_flag = data["directionFlag"]
        
    def __str__(self) -> str:
        return f"{self.name} heading {self.direction} at {self.time.time()} {self.date.date()}"
            
class BoardArrival(list):

    def __init__(self, data: dict, access_id: str):
        super().__init__([])
        for line in data["Arrival"]:
            self.append(LineArrival(line, access_id))

    def __str__(self) -> str:
        lines = []
        for line in self:
            lines.append(str(line))
        return "Arrival board\n" + "\n".join(lines)

class BoardDeparture(list):

    def __init__(self, data: dict, access_id: str):
        super().__init__([])
        for line in data["Departure"]:
            self.append(LineDeparture(line, access_id))

    def __str__(self) -> str:
        lines = []
        for line in self:
            lines.append(str(line))
        return "Departure board\n" + "\n".join(lines)