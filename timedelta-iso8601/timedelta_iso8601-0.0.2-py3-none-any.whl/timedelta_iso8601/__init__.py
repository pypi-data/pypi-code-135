import datetime
import string

_DURATION_UNITS = {
    "Y": "years",
    "M": "months",
    "D": "days",
}
_TIME_UNITS = {
    "H": "hours",
    "M": "minutes",
    "S": "seconds",
}
_WEEK_UNITS = {
    "W": "weeks",
}

_NUMERIC_CHARACTERS = frozenset(string.digits + ".,")


class timedelta(datetime.timedelta):
    def _denormalize(self):
        weeks, days, hours, minutes, seconds = 0, self.days, 0, 0, self.seconds
        weeks, days = weeks + int(days / 7), days % 7
        days, seconds = days + int(seconds / 86400), seconds % 86400
        hours, seconds = hours + int(seconds / 3600), seconds % 3600
        minutes, seconds = minutes + int(seconds / 60), seconds % 60
        return weeks, days, hours, minutes, seconds

    def isoformat(self):
        """Return the duration formatted according to ISO."""
        weeks, days, hours, minutes, seconds = self._denormalize()
        if weeks:
            if not any([days, hours, minutes, seconds]):
                return f"P{weeks}W"
            else:
                days += weeks * 7

        duration, time = str(), str()
        if days:
            duration += f"{days}D"
        if hours:
            time += f"{hours}H"
        if minutes:
            time += f"{minutes}M"
        if seconds:
            time += f"{seconds}S"
        if time:
            duration += f"T{time}"
        if duration:
            return f"P{duration}"
        else:
            return "P0D"

    @classmethod
    def fromisoformat(cls, duration_string):
        """Construct a duration from a string in ISO 8601 format."""
        if not isinstance(duration_string, str):
            raise TypeError("fromisoformat: argument must be str")

        def _invalid_format(reason):
            msg = f"Invalid isoformat string '{duration_string}': {reason}"
            return ValueError(msg)

        input = iter(duration_string)
        if next(input, None) != "P":
            raise _invalid_format("must start with the character 'P'")

        duration_designators = iter(["Y", "M", "D"])
        time_designators = iter(["H", "M", "S"])
        week_designators = iter(["W"])
        designators, units = duration_designators, _DURATION_UNITS

        measurements = dict()
        numeral = str()
        designator = None

        char = None
        for char in input:

            if char in _NUMERIC_CHARACTERS:
                numeral += "." if char == "," else char
                continue

            if designators == duration_designators and char == "T":
                designators, units = time_designators, _TIME_UNITS
                continue

            if designators == duration_designators and char == "W":
                designators, units = week_designators, _WEEK_UNITS
                pass

            designator = char if char in designators else None
            if not numeral:
                raise _invalid_format(f"missing number before '{char}'")
            if not designator:
                raise _invalid_format(f"missing designator after '{char}'")

            value = int(numeral) if numeral.isdigit() else float(numeral)
            measurements[units[designator]] = value
            numeral = str()
            designator = None

        if char == "T":
            raise _invalid_format("incomplete time-string")
        if numeral and not designator:
            raise _invalid_format("incomplete measurement at end-of-string")
        if not measurements:
            raise _invalid_format("no duration measurements found")

        try:
            return cls(**measurements)
        except TypeError:
            msg = "Unsupported: could not create timedelta for this duration"
            raise NotImplementedError(msg)
